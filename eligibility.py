from datetime import date, datetime
from typing import Dict, Any, Optional, List, Tuple

QUALIFYING_MONTH_DAYS = [
    (1, 1),   # 1st January
    (4, 1),   # 1st April
    (7, 1),   # 1st July
    (10, 1),  # 1st October
]

def parse_dob(dob_str: Optional[str]) -> Tuple[Optional[date], Optional[str]]:
    """
    Parse and validate date of birth string.
    Expected format: YYYY-MM-DD.
    Returns (parsed_date, error_message).
    """
    if not dob_str or not dob_str.strip():
        return None, "Date of birth is required."
    
    clean_str = dob_str.strip()
    try:
        parsed = datetime.strptime(clean_str, "%Y-%m-%d").date()
    except ValueError:
        return None, "Invalid date format. Please use YYYY-MM-DD."
    
    return parsed, None

def calculate_age_on_date(dob: date, target_date: date) -> Tuple[int, int, int]:
    """
    Calculate age in years, months, and days on target_date.
    Returns (years, months, days).
    """
    if target_date < dob:
        return 0, 0, 0
    
    years = target_date.year - dob.year
    months = target_date.month - dob.month
    days = target_date.day - dob.day

    if days < 0:
        # Borrow days from previous month
        prev_month = target_date.month - 1 if target_date.month > 1 else 12
        prev_year = target_date.year if target_date.month > 1 else target_date.year - 1
        # approximate days in previous month
        if prev_month in (1, 3, 5, 7, 8, 10, 12):
            borrow_days = 31
        elif prev_month == 2:
            is_leap = (prev_year % 4 == 0 and prev_year % 100 != 0) or (prev_year % 400 == 0)
            borrow_days = 29 if is_leap else 28
        else:
            borrow_days = 30
        days += borrow_days
        months -= 1

    if months < 0:
        months += 12
        years -= 1

    return max(0, years), max(0, months), max(0, days)

def get_upcoming_qualifying_dates(ref_date: date, count: int = 5) -> List[date]:
    """
    Get the next `count` qualifying dates (1 Jan, 1 Apr, 1 Jul, 1 Oct)
    on or after ref_date.
    """
    qualifying_dates = []
    year = ref_date.year
    while len(qualifying_dates) < count:
        for month, day in QUALIFYING_MONTH_DAYS:
            q_date = date(year, month, day)
            if q_date >= ref_date:
                qualifying_dates.append(q_date)
                if len(qualifying_dates) >= count:
                    break
        year += 1
    return qualifying_dates

def evaluate_voter_eligibility(
    dob_str: Optional[str],
    citizenship: bool,
    residence_confirmed: bool,
    not_disqualified: bool,
    reference_date: Optional[date] = None
) -> Dict[str, Any]:
    """
    Comprehensive voter eligibility check based on ECI guidelines and
    Section 14(b) of the Representation of the People Act, 1950.
    
    This function processes the date in-memory and does NOT store personal data.
    """
    if reference_date is None:
        reference_date = date.today()
    
    # 1. Parse and validate DOB
    dob, err = parse_dob(dob_str)
    if err:
        return {
            "success": False,
            "status_code": "INVALID_INPUT",
            "message": err,
            "details": None
        }
    
    # 2. Date sanity checks
    if dob > reference_date:
        return {
            "success": False,
            "status_code": "FUTURE_DOB",
            "message": "Date of birth cannot be in the future.",
            "details": None
        }
    
    current_years, current_months, current_days = calculate_age_on_date(dob, reference_date)
    if current_years > 120:
        return {
            "success": False,
            "status_code": "UNREALISTIC_DOB",
            "message": "Please enter a realistic date of birth (under 120 years).",
            "details": None
        }
    
    # 3. Citizenship check
    if not citizenship:
        return {
            "success": True,
            "status_code": "INELIGIBLE_CITIZENSHIP",
            "headline": "More information is needed to assess your eligibility.",
            "summary": "Under Article 326 of the Constitution of India, voter registration in the Indian electoral roll is reserved exclusively for citizens of India.",
            "qualifying_status": "Non-Citizen",
            "age_summary": f"{current_years} years, {current_months} months",
            "recommendations": [
                "Only Indian citizens who meet the age and residency conditions can enroll.",
                "If you are an Indian citizen residing abroad holding an Indian passport, you can register as an Overseas Elector using Form 6A."
            ],
            "action_button": {
                "text": "Explore Official Services",
                "url": "/official-services"
            }
        }
    
    # 4. Residence and disqualification check
    if not residence_confirmed or not not_disqualified:
        return {
            "success": True,
            "status_code": "REQUIRES_REVIEW",
            "headline": "More information is needed to assess your eligibility.",
            "summary": "To enroll in the electoral roll, you must be an ordinary resident of the constituency and not disqualified under Section 16 of the Representation of the People Act, 1950.",
            "qualifying_status": "Criteria Under Review",
            "age_summary": f"{current_years} years, {current_months} months",
            "recommendations": [
                "Ordinary Residence: You must reside at your current constituency address (generally for at least 6 months).",
                "Legal Qualifications: You must not be disqualified due to unsound mind declared by a competent court or corrupt election practices.",
                "Review the official guidelines or contact your local Electoral Registration Officer (ERO) for assistance."
            ],
            "action_button": {
                "text": "View Registration Guide",
                "url": "/registration-guide"
            }
        }
    
    # 5. Age & Qualifying Dates Analysis
    # Case A: Already 18 or older
    if current_years >= 18:
        # Determine the most recent qualifying date passed
        recent_q_dates = []
        for y in [reference_date.year - 1, reference_date.year]:
            for m, d in QUALIFYING_MONTH_DAYS:
                qd = date(y, m, d)
                if qd <= reference_date:
                    recent_q_dates.append(qd)
        last_qualifying_date = max(recent_q_dates) if recent_q_dates else date(reference_date.year, 1, 1)

        return {
            "success": True,
            "status_code": "ELIGIBLE_NOW",
            "headline": "You meet the basic age requirement.",
            "summary": f"You are {current_years} years old. You satisfy the age qualification under Indian election law.",
            "qualifying_status": "Age Requirement Met",
            "age_summary": f"{current_years} years, {current_months} months, {current_days} days",
            "reference_date_str": reference_date.strftime("%d %B %Y"),
            "effective_qualifying_date": last_qualifying_date.strftime("%d %B %Y"),
            "disclaimer": "Important: Meeting the age requirement alone does not mean you are automatically registered. You must actively submit Form 6 on the official ECI portal to be enrolled in the electoral roll.",
            "recommendations": [
                "Step 1: Gather your Proof of Age (e.g., Birth Certificate, 10th Marksheet, Aadhaar) and Proof of Residence.",
                "Step 2: Submit Form 6 online via the official Voters' Service Portal (voters.eci.gov.in).",
                "Step 3: Track your application using the official reference number.",
                "Step 4: Verify your name in the electoral roll prior to election day."
            ],
            "action_button": {
                "text": "Start Registration Guide (Form 6)",
                "url": "/registration-guide"
            }
        }
    
    # Case B: Currently under 18. Check when they turn 18.
    dob_18th = date(dob.year + 18, dob.month, dob.day)
    upcoming_q_dates = get_upcoming_qualifying_dates(reference_date, count=6)
    
    # Find the earliest qualifying date on or after their 18th birthday
    eligible_q_date = None
    for qd in upcoming_q_dates:
        if qd >= dob_18th:
            eligible_q_date = qd
            break
    
    # ECI allows advance application during the annual revision if turning 18 in the upcoming qualifying dates
    # Specifically, if turning 18 within the next 4 qualifying cycles (up to 12 months)
    days_to_18 = (dob_18th - reference_date).days
    
    if days_to_18 <= 365 and eligible_q_date:
        return {
            "success": True,
            "status_code": "ADVANCE_APPLICATION_ELIGIBLE",
            "headline": "Eligible for Advance Application under ECI Rules.",
            "summary": (
                f"You are currently {current_years} years old. You will turn 18 on {dob_18th.strftime('%d %B %Y')}. "
                f"Under the amended Representation of the People Act, citizens can apply in advance for the upcoming qualifying date of {eligible_q_date.strftime('%d %B %Y')}."
            ),
            "qualifying_status": "Advance Application Eligible",
            "age_summary": f"{current_years} years, {current_months} months ({days_to_18} days until 18th birthday)",
            "effective_qualifying_date": eligible_q_date.strftime("%d %B %Y"),
            "disclaimer": "Advance applications are processed in the quarter in which you attain the age of 18. You will be registered on the electoral roll once your eligibility date arrives.",
            "recommendations": [
                f"You will attain 18 years on {dob_18th.strftime('%d %B %Y')}.",
                f"Your official qualifying date will be {eligible_q_date.strftime('%d %B %Y')}.",
                "You can submit Form 6 in advance via the official ECI Voters' Service Portal.",
                "Keep your identity and address documents ready for quick processing."
            ],
            "action_button": {
                "text": "Learn How Advance Application Works",
                "url": "/registration-guide"
            }
        }
    
    # Case C: Younger than 17 (Future voter)
    return {
        "success": True,
        "status_code": "UNDERAGE",
        "headline": "You have not yet reached the basic voting age.",
        "summary": (
            f"You are currently {current_years} years old. In India, the legal voting age is 18 years. "
            f"You will become eligible to register when you reach 18 on {dob_18th.strftime('%d %B %Y')}."
        ),
        "qualifying_status": "Under Minimum Voting Age",
        "age_summary": f"{current_years} years, {current_months} months",
        "effective_qualifying_date": (eligible_q_date.strftime("%d %B %Y") if eligible_q_date else "Upon turning 18"),
        "disclaimer": "Voter registration opens when you turn 18 (with advance applications accepted in the year preceding your 18th birthday).",
        "recommendations": [
            f"Mark your calendar: You reach voting age on {dob_18th.strftime('%d %B %Y')}.",
            "Familiarize yourself with democratic participation, voter rights, and the electoral process.",
            "When you are within 12 months of turning 18, check back here to prepare your Form 6 advance submission!"
        ],
        "action_button": {
            "text": "Read Voter Awareness Guide",
            "url": "/faq"
        }
    }
