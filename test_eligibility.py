import unittest
from datetime import date
from eligibility import (
    evaluate_voter_eligibility,
    parse_dob,
    calculate_age_on_date,
    get_upcoming_qualifying_dates
)
from app import app
from database import init_db

class TestVoterEligibilityLogic(unittest.TestCase):
    """Unit tests for the modular voter eligibility logic and statutory rules."""

    def setUp(self):
        # Deterministic reference date: October 20, 2026
        self.ref_date = date(2026, 10, 20)

    def test_meets_basic_age_requirement(self):
        """A person aged 18 or above meets the basic voting age requirement."""
        # Born 15 May 2004 -> Age 22
        result = evaluate_voter_eligibility(
            dob_str="2004-05-15",
            citizenship=True,
            residence_confirmed=True,
            not_disqualified=True,
            reference_date=self.ref_date
        )
        self.assertTrue(result["success"])
        self.assertEqual(result["status_code"], "ELIGIBLE_NOW")
        self.assertEqual(result["headline"], "You meet the basic age requirement.")
        self.assertIn("Age Requirement Met", result["qualifying_status"])
        self.assertIn("disclaimer", result)

    def test_below_basic_age_requirement(self):
        """A person well below 17 (e.g., 14 years old) is underage."""
        # Born 10 Jan 2012 -> Age 14
        result = evaluate_voter_eligibility(
            dob_str="2012-01-10",
            citizenship=True,
            residence_confirmed=True,
            not_disqualified=True,
            reference_date=self.ref_date
        )
        self.assertTrue(result["success"])
        self.assertEqual(result["status_code"], "UNDERAGE")
        self.assertEqual(result["headline"], "You have not yet reached the basic voting age.")
        self.assertIn("Under Minimum Voting Age", result["qualifying_status"])

    def test_advance_application_qualifying_date(self):
        """
        A person who is 17 and turns 18 within the next 12 months is eligible
        for advance application for the upcoming qualifying date.
        """
        # Born 15 December 2008 -> turns 18 on 15 Dec 2026.
        # Next qualifying date on/after 18th bday is 1 Jan 2027.
        result = evaluate_voter_eligibility(
            dob_str="2008-12-15",
            citizenship=True,
            residence_confirmed=True,
            not_disqualified=True,
            reference_date=self.ref_date
        )
        self.assertTrue(result["success"])
        self.assertEqual(result["status_code"], "ADVANCE_APPLICATION_ELIGIBLE")
        self.assertIn("Eligible for Advance Application", result["headline"])
        self.assertIn("01 January 2027", result["effective_qualifying_date"])

    def test_qualifying_date_boundary_cases(self):
        """Boundary test: exactly attaining 18 on a statutory qualifying date (Jan 1, Apr 1, Jul 1, Oct 1)."""
        # Scenario 1: Turning 18 exactly on October 1st, 2026
        # Born 1 October 2008, evaluated on 1 October 2026
        result_oct = evaluate_voter_eligibility(
            dob_str="2008-10-01",
            citizenship=True,
            residence_confirmed=True,
            not_disqualified=True,
            reference_date=date(2026, 10, 1)
        )
        self.assertTrue(result_oct["success"])
        self.assertEqual(result_oct["status_code"], "ELIGIBLE_NOW")
        self.assertIn("01 October 2026", result_oct["effective_qualifying_date"])

        # Scenario 2: Turning 18 on 1st January
        # Born 1 January 2008, evaluated on 1 January 2026
        result_jan = evaluate_voter_eligibility(
            dob_str="2008-01-01",
            citizenship=True,
            residence_confirmed=True,
            not_disqualified=True,
            reference_date=date(2026, 1, 1)
        )
        self.assertTrue(result_jan["success"])
        self.assertEqual(result_jan["status_code"], "ELIGIBLE_NOW")

    def test_invalid_date_of_birth(self):
        """Invalid DOB formats and values must return appropriate error status."""
        # 1. Malformed date string
        res_malformed = evaluate_voter_eligibility(
            dob_str="invalid-date",
            citizenship=True,
            residence_confirmed=True,
            not_disqualified=True
        )
        self.assertFalse(res_malformed["success"])
        self.assertEqual(res_malformed["status_code"], "INVALID_INPUT")

        # 2. Future date
        res_future = evaluate_voter_eligibility(
            dob_str="2035-05-10",
            citizenship=True,
            residence_confirmed=True,
            not_disqualified=True,
            reference_date=self.ref_date
        )
        self.assertFalse(res_future["success"])
        self.assertEqual(res_future["status_code"], "FUTURE_DOB")

        # 3. Unrealistic date (e.g. 150 years ago)
        res_ancient = evaluate_voter_eligibility(
            dob_str="1850-01-01",
            citizenship=True,
            residence_confirmed=True,
            not_disqualified=True,
            reference_date=self.ref_date
        )
        self.assertFalse(res_ancient["success"])
        self.assertEqual(res_ancient["status_code"], "UNREALISTIC_DOB")

    def test_missing_form_fields(self):
        """Missing or empty DOB must be rejected."""
        res_none = evaluate_voter_eligibility(
            dob_str=None,
            citizenship=True,
            residence_confirmed=True,
            not_disqualified=True
        )
        self.assertFalse(res_none["success"])

        res_empty = evaluate_voter_eligibility(
            dob_str="   ",
            citizenship=True,
            residence_confirmed=True,
            not_disqualified=True
        )
        self.assertFalse(res_empty["success"])

    def test_non_citizen_handling(self):
        """Non-Indian citizens receive clear constitutional notice."""
        result = evaluate_voter_eligibility(
            dob_str="2000-01-01",
            citizenship=False,
            residence_confirmed=True,
            not_disqualified=True,
            reference_date=self.ref_date
        )
        self.assertTrue(result["success"])
        self.assertEqual(result["status_code"], "INELIGIBLE_CITIZENSHIP")
        self.assertEqual(result["headline"], "More information is needed to assess your eligibility.")

    def test_disqualification_handling(self):
        """Residency or legal disqualification triggers 'More information is needed'."""
        result = evaluate_voter_eligibility(
            dob_str="2000-01-01",
            citizenship=True,
            residence_confirmed=False,
            not_disqualified=True,
            reference_date=self.ref_date
        )
        self.assertTrue(result["success"])
        self.assertEqual(result["status_code"], "REQUIRES_REVIEW")
        self.assertEqual(result["headline"], "More information is needed to assess your eligibility.")


class TestFlaskRoutesAndSecurity(unittest.TestCase):
    """Integration tests for Flask routes, CSRF protection, and page rendering."""

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'test-secret'
        self.client = app.test_client()
        with app.app_context():
            init_db()

    def test_successful_page_loading(self):
        """All main GET endpoints must return HTTP 200 OK."""
        routes = [
            '/',
            '/eligibility',
            '/registration-guide',
            '/official-services',
            '/check-registration',
            '/faq',
            '/feedback'
        ]
        for route in routes:
            with self.subTest(route=route):
                response = self.client.get(route)
                self.assertEqual(response.status_code, 200, f"Route {route} failed to load.")
                self.assertIn(b"Smart Voter", response.data)

    def test_language_switching(self):
        """Switching language to Tamil ('ta') and English ('en') must update session."""
        res_ta = self.client.get('/set-language/ta', follow_redirects=True)
        self.assertEqual(res_ta.status_code, 200)
        with self.client.session_transaction() as sess:
            self.assertEqual(sess.get('lang'), 'ta')

        # Check that page now renders Tamil title
        self.assertIn("ஸ்மார்ட் வாக்காளர் தளம்".encode('utf-8'), res_ta.data)

        # Switch back to English
        res_en = self.client.get('/set-language/en', follow_redirects=True)
        self.assertEqual(res_en.status_code, 200)
        with self.client.session_transaction() as sess:
            self.assertEqual(sess.get('lang'), 'en')
        self.assertIn(b"Smart Voter Portal", res_en.data)

    def test_csrf_protection_on_post(self):
        """POST without CSRF token must be blocked with HTTP 400."""
        response = self.client.post('/eligibility/check', data={
            'dob': '2000-01-01',
            'citizenship': 'yes',
            'residence': 'yes',
            'not_disqualified': 'yes'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"CSRF", response.data)

    def test_successful_form_submission(self):
        """Valid eligibility form submission with CSRF token renders result card."""
        with self.client as c:
            # First GET /eligibility to establish session with CSRF token
            c.get('/eligibility')
            with c.session_transaction() as sess:
                token = sess.get('csrf_token')

            response = c.post('/eligibility/check', data={
                'csrf_token': token,
                'dob': '2004-05-15',
                'citizenship': 'yes',
                'residence': 'yes',
                'not_disqualified': 'yes'
            })
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"You meet the basic age requirement", response.data)

    def test_invalid_form_submission(self):
        """Invalid DOB or future date produces helpful message with HTTP 400."""
        with self.client as c:
            c.get('/eligibility')
            with c.session_transaction() as sess:
                token = sess.get('csrf_token')

            # Empty DOB
            response_empty = c.post('/eligibility/check', data={
                'csrf_token': token,
                'dob': '',
                'citizenship': 'yes',
                'residence': 'yes',
                'not_disqualified': 'yes'
            })
            self.assertEqual(response_empty.status_code, 400)
            self.assertIn(b"Date of birth is required", response_empty.data)

            # Future DOB
            response_future = c.post('/eligibility/check', data={
                'csrf_token': token,
                'dob': '2050-01-01',
                'citizenship': 'yes',
                'residence': 'yes',
                'not_disqualified': 'yes'
            })
            self.assertEqual(response_future.status_code, 400)
            self.assertIn(b"cannot be in the future", response_future.data)

    def test_security_headers_present(self):
        """Mandatory security headers must be present on HTTP responses."""
        response = self.client.get('/')
        self.assertEqual(response.headers.get('X-Content-Type-Options'), 'nosniff')
        self.assertEqual(response.headers.get('X-Frame-Options'), 'SAMEORIGIN')
        self.assertIn('Content-Security-Policy', response.headers)


if __name__ == '__main__':
    unittest.main()
