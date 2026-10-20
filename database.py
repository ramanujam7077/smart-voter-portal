import sqlite3
import os
from pathlib import Path
from config import Config

def get_db_path():
    db_path = Config.DATABASE_PATH
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return db_path

def get_db():
    conn = sqlite3.connect(get_db_path())
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize database tables and seed official FAQs if not already populated."""
    db_path = get_db_path()
    conn = get_db()
    cursor = conn.cursor()

    # Table: FAQs
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS faqs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        question_en TEXT NOT NULL,
        answer_en TEXT NOT NULL,
        question_ta TEXT NOT NULL,
        answer_ta TEXT NOT NULL,
        display_order INTEGER DEFAULT 0
    )
    """)

    # Table: Feedback (Anonymous user feedback)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        helpful TEXT NOT NULL,
        category TEXT,
        comment TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()

    # Seed FAQs if empty
    cursor.execute("SELECT COUNT(*) FROM faqs")
    count = cursor.fetchone()[0]
    if count == 0:
        seed_faqs(conn)

    conn.close()

def seed_faqs(conn):
    """Seed the database with verified, neutral voter information in English and Tamil."""
    faqs_data = [
        (
            "eligibility",
            "What is voter eligibility in India?",
            "Voter eligibility refers to the legal qualification required under Article 326 of the Constitution of India and the Representation of the People Act, 1950. An eligible voter must be a citizen of India, must have attained at least 18 years of age on the qualifying date, must be an ordinary resident of the constituency, and must not be disqualified under any law due to unsound mind, crime, or corrupt election practices.",
            "இந்தியாவில் வாக்காளர் தகுதி என்றால் என்ன?",
            "இந்திய அரசியலமைப்புச் சட்டத்தின் 326-வது பிரிவு மற்றும் 1950-ஆம் ஆண்டின் மக்கள் பிரதிநிதித்துவச் சட்டத்தின்படி வாக்களிக்கும் சட்டப்பூர்வ தகுதியாகும். வாக்காளர் இந்திய குடிமகனாக இருக்க வேண்டும், தகுதி தேதியில் குறைந்தது 18 வயதை பூர்த்தி செய்திருக்க வேண்டும், சம்மந்தப்பட்ட தொகுதியின் சாதாரண குடியிருப்பாளராக இருக்க வேண்டும், மேலும் நீதிமன்றத்தால் தகுதியற்றவர் என அறிவிக்கப்படாதவராக இருக்க வேண்டும்.",
            1
        ),
        (
            "eligibility",
            "What is the minimum voting age in India?",
            "The minimum voting age in India is 18 years. It was lowered from 21 to 18 years in 1988 by the 61st Constitutional Amendment Act, empowering Indian youth to actively participate in the democratic process.",
            "இந்தியாவில் வாக்களிப்பதற்கான குறைந்தபட்ச வயது என்ன?",
            "இந்தியாவில் வாக்களிப்பதற்கான குறைந்தபட்ச வயது 18 ஆகும். 1988-ஆம் ஆண்டின் 61-வது அரசியலமைப்பு திருத்தச் சட்டம் மூலம் வாக்குரிமை வயது 21-லிருந்து 18 ஆக குறைக்கப்பட்டது.",
            2
        ),
        (
            "eligibility",
            "What are the four qualifying dates for voter registration?",
            "Following the 2022 amendment to the Representation of the People Act, 1950, there are four qualifying dates each year: 1st January, 1st April, 1st July, and 1st October. Citizens who turn 18 on or before any of these dates can register, and youth can even submit advance applications in the quarter before turning 18.",
            "வாக்காளர் பதிவுக்கான நான்கு தகுதி தேதிகள் யாவை?",
            "1950-ஆம் ஆண்டின் மக்கள் பிரதிநிதித்துவச் சட்டத்தில் 2022-ல் கொண்டுவரப்பட்ட திருத்தத்தின்படி, ஆண்டுக்கு நான்கு தகுதி தேதிகள் உள்ளன: ஜனவரி 1, ஏப்ரல் 1, ஜூலை 1 மற்றும் அக்டோபர் 1. இந்த தேதிகளில் அல்லது அதற்கு முன் 18 வயதை எட்டும் குடிமக்கள் பதிவு செய்யலாம். மேலும் 17 வயது நிறைவடைந்தவர்கள் முன்கூட்டியே விண்ணப்பிக்கலாம்.",
            3
        ),
        (
            "registration",
            "Is voter registration automatic when someone turns 18?",
            "No, voter registration is NOT automatic. Even though you legally become eligible at age 18, you must actively apply by submitting Form 6 through the official Election Commission of India portal (voters.eci.gov.in), the Voter Helpline App, or via your local Booth Level Officer (BLO).",
            "ஒருவர் 18 வயதை எட்டும்போது வாக்காளர் பதிவு தானாகவே நடக்குமா?",
            "இல்லை, வாக்காளர் பதிவு தானாக நடைபெறாது. 18 வயதை பூர்த்தி செய்தவுடன், இந்திய தேர்தல் ஆணையத்தின் அதிகாரப்பூர்வ இணையதளம் (voters.eci.gov.in), Voter Helpline செயலி அல்லது வாக்குச்சாவடி நிலை அலுவலர் (BLO) மூலமாக படிவம் 6 (Form 6) சமர்ப்பித்து பதிவு செய்ய வேண்டும்.",
            4
        ),
        (
            "registration",
            "How can I register as a first-time voter?",
            "To register as a first-time voter: 1. Visit voters.eci.gov.in or download the Voter Helpline App. 2. Sign up with your mobile number. 3. Fill Form 6 (Application for New Voters). 4. Upload a recent photograph, valid Proof of Age, and Proof of Ordinary Residence. 5. Submit and save your Application Reference Number to track status.",
            "முதல்முறை வாக்காளராக நான் எவ்வாறு பதிவு செய்வது?",
            "முதல்முறை வாக்காளராக பதிவு செய்ய: 1. voters.eci.gov.in தளத்திற்கு செல்லவும் அல்லது Voter Helpline செயலியை பதிவிறக்கவும். 2. மொபைல் எண் மூலம் உள்நுழையவும். 3. புதிய வாக்காளர்களுக்கான படிவம் 6-ஐ நிரப்பவும். 4. புகைப்படமும், வயது மற்றும் முகவரி சான்றுகளையும் பதிவேற்றவும். 5. சமர்ப்பித்து, நிலை அறிய குறிப்பு எண்ணை (Reference Number) குறித்துக்கொள்ளவும்.",
            5
        ),
        (
            "verification",
            "How can I check whether my name is on the electoral roll?",
            "You can verify your name on the official electoral roll anytime via electoralsearch.eci.gov.in or the Voter Helpline App. You can search using: 1. Your EPIC (Voter ID) number, 2. Personal details (Name, Age, State, District, Assembly Constituency), or 3. Mobile Number with OTP verification.",
            "வாக்காளர் பட்டியலில் எனது பெயர் உள்ளதா என்பதை எப்படி சரிபார்ப்பது?",
            "electoralsearch.eci.gov.in என்ற அதிகாரப்பூர்வ இணையதளம் அல்லது Voter Helpline ஆப் மூலம் சரிபார்க்கலாம். 1. EPIC (வாக்காளர் அடையாள அட்டை) எண், 2. தனிப்பட்ட விவரங்கள் (பெயர், வயது, தொகுதி), அல்லது 3. மொபைல் எண் (OTP) மூலமாக உடனடியாக தேடலாம்.",
            6
        ),
        (
            "verification",
            "What should I do if my name is missing from the electoral roll?",
            "If your name is not in the electoral roll, you cannot vote on polling day—even if you possess a physical Voter ID card. You must immediately apply for inclusion by filing Form 6 on voters.eci.gov.in during the continuous updation period or Special Summary Revision.",
            "வாக்காளர் பட்டியலில் எனது பெயர் விடுபட்டிருந்தால் என்ன செய்வது?",
            "வாக்காளர் பட்டியலில் உங்கள் பெயர் இல்லை என்றால் வாக்குச்சாவடியில் வாக்களிக்க முடியாது. எனவே உடனே voters.eci.gov.in மூலம் படிவம் 6 சமர்ப்பித்து உங்கள் பெயரை சேர்க்க விண்ணப்பிக்க வேண்டும்.",
            7
        ),
        (
            "rules",
            "Can I vote if I have a voter ID card but my name is NOT on the electoral roll?",
            "NO. Under Indian election rules, possessing a physical Voter ID card (EPIC) alone does not entitle you to vote. Your name MUST appear in the official electoral roll of your polling booth on election day. Always verify your name prior to polling day.",
            "வாக்காளர் அடையாள அட்டை இருந்தும் பெயர் பட்டியலில் இல்லையென்றால் வாக்களிக்க முடியுமா?",
            "முடியாது! வாக்காளர் அடையாள அட்டை (EPIC) வைத்திருந்தாலும், தேர்தல் நாளன்று வாக்குச்சாவடி வாக்காளர் பட்டியலில் உங்கள் பெயர் இருப்பது கட்டாயமாகும். எனவே முன்கூட்டியே பட்டியலில் பெயர் உள்ளதா என்பதை சரிபார்த்துக் கொள்ளவும்.",
            8
        ),
        (
            "registration",
            "What documents are officially accepted for voter registration?",
            "Age Proof: Birth Certificate, Aadhaar Card, PAN Card, Driving Licence, Indian Passport, or Class 10/12 Marksheet with DOB. Residence Proof: Water/Electricity/Gas connection bill (1 year), Aadhaar Card, Current Bank/Post Office Passbook, Indian Passport, or Registered Rent/Sale Deed.",
            "வாக்காளர் பதிவுக்கு அதிகாரப்பூர்வமாக ஏற்றுக்கொள்ளப்படும் ஆவணங்கள் எவை?",
            "வயது சான்று: பிறப்பு சான்றிதழ், ஆதார் அட்டை, பான் கார்டு, ஓட்டுநர் உரிமம், பாஸ்போர்ட், அல்லது 10/12 ஆம் வகுப்பு மதிப்பெண் சான்றிதழ். முகவரி சான்று: மின்சாரம்/நீர்/எரிவாயு கட்டண ரசீது, ஆதார் அட்டை, வங்கி/அஞ்சலக கணக்குப் புத்தகம், பாஸ்போர்ட், அல்லது பதிவு செய்யப்பட்ட வாடகை/விற்பனை பத்திரம்.",
            9
        ),
        (
            "services",
            "What is the official Voter Helpline Number and App?",
            "The official National Contact Centre toll-free helpline number is 1950 (accessible across India). The official mobile app is the 'Voter Helpline App' created by the Election Commission of India, available on both Google Play Store and Apple App Store.",
            "அதிகாரப்பூர்வ வாக்காளர் உதவி எண் மற்றும் செயலி என்ன?",
            "அனைத்து மாநிலங்களுக்கும் கட்டணமில்லா உதவி எண்: 1950. இந்திய தேர்தல் ஆணையத்தின் அதிகாரப்பூர்வ மொபைல் செயலி 'Voter Helpline App' ஆகும். இது கூகுள் பிளே ஸ்டோர் மற்றும் ஆப்பிள் ஆப் ஸ்டோரில் கிடைக்கிறது.",
            10
        )
    ]

    cursor = conn.cursor()
    cursor.executemany("""
    INSERT INTO faqs (category, question_en, answer_en, question_ta, answer_ta, display_order)
    VALUES (?, ?, ?, ?, ?, ?)
    """, faqs_data)
    conn.commit()

def get_faqs(category=None):
    """Fetch FAQs, optionally filtered by category."""
    conn = get_db()
    cursor = conn.cursor()
    if category and category != 'all':
        cursor.execute("SELECT * FROM faqs WHERE category = ? ORDER BY display_order ASC", (category,))
    else:
        cursor.execute("SELECT * FROM faqs ORDER BY display_order ASC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def save_feedback(helpful, category, comment):
    """Save anonymous user feedback."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO feedback (helpful, category, comment)
    VALUES (?, ?, ?)
    """, (helpful, category, comment))
    conn.commit()
    conn.close()

def get_feedback_count():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM feedback")
    count = cursor.fetchone()[0]
    conn.close()
    return count
