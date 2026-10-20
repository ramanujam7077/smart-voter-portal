# Smart Voter Eligibility and Registration Assistance Portal

A modern, responsive, citizen-first civic web application built with Python Flask and vanilla CSS/JS to assist first-time voters, youth, and citizens across India in understanding voter eligibility requirements, navigating the 4 statutory qualifying dates, preparing Form 6 registration documents, and accessing verified Election Commission of India (ECI) services.

> **CRITICAL LEGAL NOTICE & DISCLAIMER**  
> This portal is an educational and civic-assistance project. It is **NOT** operated by, affiliated with, or endorsed by the Election Commission of India (ECI) or any governmental authority. This portal is **NOT** an online voting or ballot-casting system. It does not issue Voter ID (EPIC) cards or register voters directly. All official voter registrations and electoral-roll searches must be submitted exclusively on official government platforms ([voters.eci.gov.in](https://voters.eci.gov.in/) / [electoralsearch.eci.gov.in](https://electoralsearch.eci.gov.in/)).

---

## Features & Capabilities

1. **Four Statutory Qualifying Dates Calculator**:
   - Implements Section 14(b) of the *Representation of the People Act, 1950* (as amended in 2022).
   - Dynamically evaluates eligibility against the 4 annual qualifying dates: **1st January, 1st April, 1st July, and 1st October**.
   - Identifies advance application eligibility for 17-year-olds turning 18 during the upcoming revision quarters.

2. **Strict Privacy Architecture**:
   - Evaluates Date of Birth strictly in-memory and immediately discards it.
   - **Zero personal identifiers collected**: Never asks for Aadhaar numbers, EPIC numbers, phone passwords, or OTPs.

3. **Step-by-Step Registration Guide (Form 6 & Form 8)**:
   - 6 sequential phases from qualification to electoral roll verification.
   - Interactive document preparation checklist distinguishing officially required documents from accepted alternatives (age proofs and residence proofs).

4. **Verified Official Election Services Directory**:
   - Direct, authentic links to `voters.eci.gov.in`, `electoralsearch.eci.gov.in`, `eci.gov.in`, the official **Voter Helpline App** (Android & iOS), and the **1950** Toll-Free Helpline.

5. **Electoral Roll Verification Guidance**:
   - Clear instructions on 3 official search methods: Search by Details, Search by EPIC, and Search by Mobile OTP.
   - Actionable troubleshooting for missing names, incorrect entries, and residential shifting.

6. **Bilingual Support (English & தமிழ் / Tamil)**:
   - Seamless one-click language toggle across all navigation, eligibility results, and FAQ content.
   - Preserves legal and constitutional precision in both languages.

7. **Security & Robustness**:
   - Session-based CSRF protection on form submissions.
   - Secure HTTP headers (`X-Frame-Options`, `X-Content-Type-Options`, `Content-Security-Policy`, `Referrer-Policy`).
   - Clean custom 400, 404, and 500 error pages with zero stack trace exposure.

---

## Project Structure

```
smart-voter-portal/
├── app.py                 # Core Flask application, route handlers & security middleware
├── config.py              # Configuration classes (Development, Testing, Production)
├── eligibility.py         # Modular voter eligibility logic & statutory date engine
├── database.py            # SQLite schema initialization & bilingual FAQ seeding
├── translations.py        # Bilingual (English/Tamil) civic dictionary
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation & deployment guide
├── instance/
│   └── portal.db          # SQLite database (auto-created on first run)
├── static/
│   ├── css/
│   │   └── style.css      # Indian election civic-tech design system (Navy, Saffron, Green)
│   ├── js/
│   │   └── main.js        # Mobile menu, FAQ accordion, search filter & checklist
│   └── images/
│       └── logo.svg       # Civic ballot & tricolor SVG badge
├── templates/
│   ├── base.html          # Base layout with navbar, footer & legal disclaimer
│   ├── index.html         # Hero landing page & feature highlights
│   ├── eligibility.html   # Interactive voter eligibility form
│   ├── eligibility_result.html # Detailed eligibility assessment card
│   ├── registration_guide.html # Step-by-step Form 6 guide & interactive checklist
│   ├── official_services.html  # Verified ECI links & helpline info
│   ├── check_registration.html # Electoral roll search guidance & troubleshooting
│   ├── faq.html           # Bilingual FAQ with real-time keyword search
│   ├── feedback.html      # Anonymous citizen feedback form
│   ├── 404.html           # Friendly 404 page
│   └── 500.html           # Friendly 500 page
└── tests/
    ├── __init__.py
    └── test_eligibility.py # Comprehensive unit & integration test suite (14 tests)
```

---

## Installation & Local Run Instructions

### 1. Prerequisites
- Python 3.9+ (Python 3.11 recommended)
- `pip` package manager

### 2. Clone or Navigate to the Project
```bash
cd /path/to/smart-voter-portal
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask Development Server
```bash
python app.py
```
The application will start at:  
👉 **http://127.0.0.1:5000** (or http://localhost:5000)

---

## Running the Automated Test Suite

The test suite covers:
- Persons meeting the basic age requirement (18+)
- Persons below the minimum voting age
- Advance application eligibility for 17-year-olds
- Qualifying-date boundary cases (turning 18 exactly on Jan 1 or Oct 1)
- Invalid dates (future dates, malformed inputs, unrealistic age)
- Non-citizen and disqualification scenarios
- CSRF validation on mutating POST endpoints
- Bilingual language toggle (English/Tamil)
- Successful page rendering across all endpoints

Run tests with Python's built-in `unittest` runner:
```bash
python -m unittest discover tests
```

Expected output:
```
..............
----------------------------------------------------------------------
Ran 14 tests in 0.16s

OK
```

---

## Environment Variables Configuration

In production, never use default keys or enable debug mode. Configure the following environment variables:

| Variable | Description | Example / Recommended Value |
| :--- | :--- | :--- |
| `FLASK_ENV` | Environment mode (`development` or `production`) | `production` |
| `SECRET_KEY` | High-entropy secret key for session & CSRF signing | Generate via `python -c "import secrets; print(secrets.token_hex(32))"` |
| `PORT` | HTTP port on which the server listens | `5000` (or injected by hosting platform) |

---

## Production Deployment Guidelines

### Option A: Deploying with Gunicorn (Linux / Cloud VM / Docker)
Install Gunicorn:
```bash
pip install gunicorn
```
Run using 4 worker processes:
```bash
gunicorn --workers 4 --bind 0.0.0.0:5000 --access-logfile - --error-logfile - app:app
```

### Option B: Deploying to Render / Railway / Heroku
1. Ensure `requirements.txt` contains:
   ```
   Flask>=3.0.0
   python-dotenv>=1.0.0
   gunicorn>=21.0.0
   ```
2. Add a `Procfile`:
   ```
   web: gunicorn app:app
   ```
3. Set Environment Variables in your hosting dashboard:
   - `FLASK_ENV=production`
   - `SECRET_KEY=<your-generated-random-token>`

---

## License & Attribution

Released under the MIT License for educational and civic empowerment purposes. All official voter forms and election regulations referenced belong to the Election Commission of India.
