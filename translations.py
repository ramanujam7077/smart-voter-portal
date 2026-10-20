"""
Bilingual (English / Tamil) translation dictionary for Smart Voter Portal.
Accurately preserves constitutional, election law, and civic terminology.
"""

TRANSLATIONS = {
    'en': {
        # Navigation
        'portal_title': 'Smart Voter Portal',
        'portal_subtitle': 'Civic Eligibility & Registration Assistance',
        'nav_home': 'Home',
        'nav_eligibility': 'Check Eligibility',
        'nav_guide': 'Registration Guide',
        'nav_services': 'Official Services',
        'nav_check_status': 'Electoral Roll Search',
        'nav_faq': 'FAQs & Awareness',
        'nav_feedback': 'Feedback',
        'lang_toggle': 'தமிழ்',
        'lang_current': 'English',

        # Hero
        'hero_badge': 'Official ECI Rules & Representation of the People Act 1950',
        'hero_title': 'Your Vote. Your Voice. Your Right.',
        'hero_description': 'A citizen-first civic guidance platform designed for first-time voters and youth across India. Understand eligibility rules, qualify through the 4 official qualifying dates, prepare required documents, and access verified Election Commission of India services.',
        'hero_cta_check': 'Check My Eligibility',
        'hero_cta_guide': 'How to Register (Form 6)',
        'hero_notice': 'Free civic service • No Aadhaar or Voter ID numbers collected • Unofficial guide for citizen empowerment',

        # Features
        'features_heading': 'How This Portal Helps You',
        'features_subheading': 'Navigating voter registration in India shouldn’t be confusing. Here is what you can do:',
        
        'card1_title': 'Instant Eligibility Checker',
        'card1_desc': 'Calculate your exact age and verify which of the 4 statutory qualifying dates (Jan 1, Apr 1, Jul 1, Oct 1) applies to you. Know if you qualify for advance application.',
        'card1_btn': 'Check Eligibility Now',

        'card2_title': 'Voter Registration Guide',
        'card2_desc': 'Step-by-step guidance for Form 6 (New Voter) and Form 8 (Correction). Includes an interactive document checklist for age and residence proof.',
        'card2_btn': 'Read Step-by-Step Guide',

        'card3_title': 'Verified Election Services',
        'card3_desc': 'Direct verified links to the official ECI Voters\' Service Portal, Voter Helpline App, National Contact Centre (1950), and Electoral Roll Search.',
        'card3_btn': 'Access Official Portals',

        # Step by Step
        'steps_heading': 'Your 4-Step Journey to Becoming an Empowered Voter',
        'step1_title': '1. Check Eligibility',
        'step1_desc': 'Confirm your citizenship, residential constituency, and age qualification against the official statutory dates.',
        'step2_title': '2. Prepare Documents',
        'step2_desc': 'Collect valid proof of age (10th marksheet, birth certificate, Aadhaar) and proof of ordinary residence.',
        'step3_title': '3. Submit Form 6 on ECI Portal',
        'step3_desc': 'Fill your application on the official Voters\' Service Portal (voters.eci.gov.in) or Voter Helpline App.',
        'step4_title': '4. Verify in Electoral Roll',
        'step4_desc': 'Track your reference number and verify your entry in the electoral roll prior to election day.',

        # Awareness
        'awareness_heading': 'Why Every First-Time Vote Matters',
        'awareness_subheading': 'Democracy thrives when young citizens participate with clarity and conviction.',
        'fact1_title': 'Four Qualifying Dates Every Year',
        'fact1_desc': 'Under Section 14(b) of the RPA 1950 (amended in 2022), you no longer have to wait a full year if you turn 18 after January 1st! You can qualify on Jan 1, Apr 1, Jul 1, or Oct 1.',
        'fact2_title': 'Voter ID Is Not Enough — Roll Entry Is Mandatory',
        'fact2_desc': 'Crucial truth: Holding an EPIC card does NOT allow you to vote if your name is not on the official polling booth electoral roll. Always verify beforehand.',
        'fact3_title': 'Advance Applications Accepted',
        'fact3_desc': 'Citizens who are 17 years old can submit Form 6 in advance during the annual revision. Your registration activates as soon as you attain 18.',

        # Eligibility Form
        'elig_title': 'Voter Eligibility Checker',
        'elig_subtitle': 'Evaluate your voter eligibility under Indian Election Law and the 4 statutory qualifying dates.',
        'elig_privacy_badge': 'Strict Privacy: Date of birth is calculated in-memory and discarded. No personal identifiers or Aadhaar collected.',
        'field_dob_label': 'Date of Birth',
        'field_dob_hint': 'Enter your date of birth as recorded in official records (e.g., Birth Certificate or 10th Certificate).',
        'field_country_label': 'Country / Jurisdiction',
        'field_country_val': 'India (Constitutional Scope: Article 326)',
        'field_citizenship_label': 'Are you a citizen of India?',
        'field_residence_label': 'Are you an ordinary resident of the constituency where you wish to enroll?',
        'field_residence_hint': 'Ordinary residence implies where you customarily reside. Students may choose either home or hostel address.',
        'field_disqualified_label': 'You confirm you are of sound mind and not disqualified under Section 16 of the RPA 1950?',
        'field_disqualified_hint': 'Section 16 disqualifies individuals declared of unsound mind by a competent court or convicted of election offences.',
        'btn_check_eligibility': 'Calculate My Eligibility',
        'btn_reset': 'Clear Form',

        # Results
        'result_title': 'Eligibility Assessment Result',
        'result_age_evaluated': 'Age Evaluated As Of',
        'result_qualifying_date': 'Applicable Qualifying Date',
        'result_disclaimer': 'Official Notice: This assessment is an educational civic tool based on Section 14(b) of the Representation of the People Act, 1950. Meeting the age condition does not constitute electoral enrollment. You must file Form 6 on the official ECI portal.',
        'result_btn_guide': 'Proceed to Registration Guide (Form 6)',
        'result_btn_recheck': 'Check Another Date of Birth',

        # Guide
        'guide_title': 'Comprehensive Voter Registration Guide',
        'guide_subtitle': 'Everything first-time voters and youth need to submit Form 6 successfully.',
        'guide_official_banner': 'Applications must be submitted exclusively on the official Election Commission of India portal: voters.eci.gov.in',
        'doc_checklist_title': 'Document Preparation Checklist',
        'doc_checklist_desc': 'Tick the documents you have ready before beginning your online registration on the official portal:',
        'doc_age_heading': '1. Proof of Age (Any ONE officially accepted document)',
        'doc_res_heading': '2. Proof of Ordinary Residence (Any ONE officially accepted document)',
        'doc_photo_heading': '3. Recent Passport Size Color Photograph (Max 2MB, white background)',

        # Official Services
        'services_title': 'Verified Official Election Services',
        'services_subtitle': 'Direct, authenticated gateways to the Election Commission of India and State Election authorities.',
        'services_notice': 'All links below lead directly to authentic government domains (*.gov.in, *.nic.in). This portal does not simulate, capture, or store official transactions.',

        # Check Registration Status
        'check_title': 'How to Verify Your Name in the Electoral Roll',
        'check_subtitle': 'Ensure your name is active on the official voter list before election day.',
        'check_methods_title': 'Three Ways to Search the Official Electoral Roll',
        'check_method1_title': 'Method 1: Search by Details',
        'check_method1_desc': 'Search using your Name, Relative\'s Name, Age/DOB, Gender, State, District, and Assembly Constituency.',
        'check_method2_title': 'Method 2: Search by EPIC (Voter ID Number)',
        'check_method2_desc': 'Enter your 10-digit alphanumeric EPIC number (e.g., ABC1234567) and State for instant booth details.',
        'check_method3_title': 'Method 3: Search by Mobile Number',
        'check_method3_desc': 'Verify using your mobile number registered with your Form 6 application via one-time SMS OTP.',
        'check_action_btn': 'Open Official Electoral Roll Search (electoralsearch.eci.gov.in)',

        # FAQ & Awareness
        'faq_title': 'Voter Awareness & Frequently Asked Questions',
        'faq_subtitle': 'Get factual, verified answers to common questions about voting rights, eligibility, and procedures in India.',
        'faq_filter_all': 'All Questions',
        'faq_filter_eligibility': 'Eligibility & Age',
        'faq_filter_registration': 'Registration & Form 6',
        'faq_filter_verification': 'Roll Search & Verification',
        'faq_filter_rules': 'Rules & Disqualifications',
        'faq_filter_services': 'Helpline & Apps',
        'faq_search_placeholder': 'Type keywords to search FAQs (e.g., age, 18, Form 6, missing name)...',

        # Feedback
        'feedback_title': 'Anonymous Citizen Feedback',
        'feedback_subtitle': 'Help us improve this civic assistance guide. We do not collect names or personal identifiers.',
        'feedback_helpful_label': 'Was this portal helpful in clarifying voter eligibility and registration?',
        'feedback_opt_yes': 'Yes, very clear and helpful',
        'feedback_opt_somewhat': 'Somewhat helpful, could be improved',
        'feedback_opt_no': 'No, I did not find what I needed',
        'feedback_category_label': 'Which area are you providing feedback on?',
        'feedback_comment_label': 'Your Suggestions or Feedback (Optional)',
        'feedback_submit': 'Submit Feedback',

        # Footer
        'footer_about_title': 'Smart Voter Portal',
        'footer_about_desc': 'An independent, non-partisan civic-tech educational initiative built to empower first-time voters and youth across India. Designed to reduce registration confusion and raise democratic awareness.',
        'footer_quick_links': 'Quick Navigation',
        'footer_official_links': 'Official Portals',
        'footer_disclaimer_title': 'Official Legal Disclaimer',
        'footer_disclaimer_text': 'DISCLAIMER: This portal is an educational and civic-assistance initiative and is NOT operated by, affiliated with, or endorsed by the Election Commission of India (ECI) or any government agency. This portal does NOT cast ballots, issue voter identity cards, or register voters directly. All official voter registrations and electoral-roll searches must be performed exclusively on official government platforms (voters.eci.gov.in / electoralsearch.eci.gov.in).',
        'footer_copyright': 'Smart Voter Eligibility & Registration Assistance Portal. Released for civic education and democratic participation.'
    },

    'ta': {
        # Navigation
        'portal_title': 'ஸ்மார்ட் வாக்காளர் தளம்',
        'portal_subtitle': 'வாக்காளர் தகுதி மற்றும் பதிவு உதவி தளம்',
        'nav_home': 'முகப்பு',
        'nav_eligibility': 'தகுதி சரிபார்ப்பு',
        'nav_guide': 'பதிவு வழிகாட்டி',
        'nav_services': 'அதிகாரப்பூர்வ சேவைகள்',
        'nav_check_status': 'வாக்காளர் பட்டியல் தேடல்',
        'nav_faq': 'கேள்வி-பதில்கள் & விழிப்புணர்வு',
        'nav_feedback': 'கருத்துகள்',
        'lang_toggle': 'English',
        'lang_current': 'தமிழ்',

        # Hero
        'hero_badge': 'இந்திய தேர்தல் ஆணைய விதிகள் மற்றும் மக்கள் பிரதிநிதித்துவ சட்டம் 1950',
        'hero_title': 'உங்கள் வாக்கு. உங்கள் குரல். உங்கள் உரிமை.',
        'hero_description': 'இந்தியாவில் உள்ள முதல்முறை வாக்காளர்கள் மற்றும் இளைஞர்களுக்கான குடிமக்கள் வழிகாட்டி தளம். வாக்காளர் தகுதி விதிகளைப் புரிந்து கொள்ளவும், 4 சட்டப்பூர்வ தகுதி தேதிகள் மூலம் தகுதி பெறவும், ஆவணங்களைத் தயார் செய்து இந்திய தேர்தல் ஆணையத்தின் சேவைகளைப் பெறவும் உதவும்.',
        'hero_cta_check': 'எனது தகுதியை சரிபார்க்க',
        'hero_cta_guide': 'எவ்வாறு பதிவு செய்வது (படிவம் 6)',
        'hero_notice': 'இலவச குடிமக்கள் சேவை • ஆதார் அல்லது வாக்காளர் அட்டை எண்கள் சேகரிக்கப்படுவதில்லை • பொது விழிப்புணர்வுக்கான வழிகாட்டி',

        # Features
        'features_heading': 'இத்தளம் உங்களுக்கு எவ்வாறு உதவுகிறது?',
        'features_subheading': 'இந்தியாவில் வாக்காளர் பதிவு பற்றிய குழப்பங்களை நீக்கி எளிதாக வழிகாட்டுகிறோம்:',

        'card1_title': 'உடனடி தகுதி சரிபார்ப்பான்',
        'card1_desc': 'உங்கள் துல்லியமான வயதை கணக்கிட்டு, 4 சட்டப்பூர்வ தகுதி தேதிகளில் (ஜனவரி 1, ஏப்ரல் 1, ஜூலை 1, அக்டோபர் 1) எது உங்களுக்கு பொருந்தும் என்பதை அறியுங்கள். முன்கூட்டியே விண்ணப்பிக்க முடியுமா என்பதை தெரிந்து கொள்ளுங்கள்.',
        'card1_btn': 'இப்போதே தகுதியை சரிபார்க்கவும்',

        'card2_title': 'வாக்காளர் பதிவு வழிகாட்டி',
        'card2_desc': 'புதிய வாக்காளர்களுக்கான படிவம் 6 மற்றும் திருத்தங்களுக்கான படிவம் 8 பற்றிய விரிவான படிப்படியான வழிகாட்டல். வயது மற்றும் முகவரி சான்றுகளுக்கான சரிபார்ப்புப் பட்டியல்.',
        'card2_btn': 'வழிகாட்டியைப் படிக்கவும்',

        'card3_title': 'அதிகாரப்பூர்வ தேர்தல் சேவைகள்',
        'card3_desc': 'இந்திய தேர்தல் ஆணையத்தின் Voters\' Service Portal, Voter Helpline செயலி, 1950 கட்டணமில்லா உதவி எண் மற்றும் வாக்காளர் பட்டியல் தேடலுக்கான நேரடி இணைப்புகள்.',
        'card3_btn': 'அதிகாரப்பூர்வ தளங்களை அணுகவும்',

        # Step by Step
        'steps_heading': 'வாக்காளராவதற்கான 4 முக்கிய படிகள்',
        'step1_title': '1. தகுதியை சரிபார்க்கவும்',
        'step1_desc': 'உங்கள் குடியுரிமை, தொகுதி இருப்பிடம் மற்றும் தகுதி தேதிக்கான வயதை உறுதிப்படுத்தவும்.',
        'step2_title': '2. ஆவணங்களைத் தயார் செய்யவும்',
        'step2_desc': 'வயது சான்று (10-ஆம் வகுப்பு சான்றிதழ், பிறப்பு சான்றிதழ், ஆதார்) மற்றும் இருப்பிட சான்றுகளை தயார் செய்யவும்.',
        'step3_title': '3. படிவம் 6-ஐ சமர்ப்பிக்கவும்',
        'step3_desc': 'அதிகாரப்பூர்வ ECI இணையதளம் (voters.eci.gov.in) அல்லது Voter Helpline செயலி மூலம் விண்ணப்பிக்கவும்.',
        'step4_title': '4. வாக்காளர் பட்டியலில் சரிபார்க்கவும்',
        'step4_desc': 'விண்ணப்பக் குறிப்பு எண்ணைக் கொண்டு நிலையை அறிந்து, தேர்தல் நாளுக்கு முன் பட்டியலில் பெயர் உள்ளதை உறுதிப்படுத்தவும்.',

        # Awareness
        'awareness_heading': 'முதல்முறை வாக்கு ஏன் மிகவும் முக்கியம்?',
        'awareness_subheading': 'இளைஞர்கள் தீவிரமாக பங்கேற்கும் போது மட்டுமே ஜனநாயகம் வலுவடைகிறது.',
        'fact1_title': 'ஆண்டுக்கு நான்கு தகுதி தேதிகள்',
        'fact1_desc': '1950-ஆம் ஆண்டின் மக்கள் பிரதிநிதித்துவ சட்டத்தின் 2022-ஆம் ஆண்டு திருத்தத்தின்படி, ஜனவரி 1-ஐ தவிர்த்து ஏப்ரல் 1, ஜூலை 1, அக்டோபர் 1 ஆகிய தேதிகளிலும் தகுதி பெறலாம்.',
        'fact2_title': 'அடையாள அட்டை மட்டும் போதாது — பட்டியலில் பெயர் அவசியம்',
        'fact2_desc': 'மிக முக்கியமான உண்மை: வாக்காளர் அடையாள அட்டை (EPIC) இருந்தாலும், வாக்குச்சாவடி பட்டியலில் உங்கள் பெயர் இல்லை என்றால் வாக்களிக்க முடியாது. முன்கூட்டியே சரிபார்க்கவும்.',
        'fact3_title': 'முன்கூட்டியே விண்ணப்பிக்கும் வாய்ப்பு',
        'fact3_desc': '17 வயது நிறைவடைந்த இளைஞர்கள் முன்கூட்டியே படிவம் 6 சமர்ப்பிக்கலாம். உங்களுக்கு 18 வயது நிறைவடைந்ததும் விண்ணப்பம் பரிசீலிக்கப்படும்.',

        # Eligibility Form
        'elig_title': 'வாக்காளர் தகுதி சரிபார்ப்பான்',
        'elig_subtitle': 'இந்திய தேர்தல் சட்டம் மற்றும் 4 சட்டப்பூர்வ தகுதி தேதிகளின் கீழ் உங்கள் தகுதியை கணக்கிடுங்கள்.',
        'elig_privacy_badge': 'கண்டிப்பான தனியுரிமை: பிறந்த தேதி நினைவகத்தில் தற்காலிகமாக கணக்கிடப்பட்டு அழிக்கப்படுகிறது. எந்த தனிப்பட்ட அடையாளமும் சேமிக்கப்படுவதில்லை.',
        'field_dob_label': 'பிறந்த தேதி',
        'field_dob_hint': 'அதிகாரப்பூர்வ ஆவணங்களில் (பிறப்பு சான்றிதழ் அல்லது 10-ஆம் வகுப்பு சான்றிதழ்) உள்ளவாறு உள்ளிடவும்.',
        'field_country_label': 'நாடு / ஆளுகை எல்லை',
        'field_country_val': 'இந்தியா (அரசியலமைப்புப் பிரிவு: 326)',
        'field_citizenship_label': 'நீங்கள் இந்திய குடிமகனா?',
        'field_residence_label': 'நீங்கள் வாக்களிக்க விரும்பும் தொகுதியின் சாதாரண குடியிருப்பாளரா?',
        'field_residence_hint': 'சாதாரண குடியிருப்பு என்பது வழக்கமாக நீங்கள் வாழும் இடத்தை குறிக்கும்.',
        'field_disqualified_label': 'நீங்கள் மனநலம் உள்ளவர் என்றும், சட்டப்படி தகுதி நீக்கம் செய்யப்படாதவர் என்றும் உறுதிப்படுத்துகிறீர்களா?',
        'field_disqualified_hint': 'நீதிமன்றத்தால் மனநலம் சரியில்லாதவர் என அறிவிக்கப்பட்டவர்கள் அல்லது தேர்தல் குற்றங்களில் தண்டனை பெற்றவர்கள் தகுதியற்றவர்கள் ஆவர்.',
        'btn_check_eligibility': 'எனது தகுதியை கணக்கிடு',
        'btn_reset': 'படிவத்தை மீட்டமைக்க',

        # Results
        'result_title': 'தகுதி மதிப்பீட்டு முடிவு',
        'result_age_evaluated': 'மதிப்பிடப்பட்ட வயது கணக்கீட்டு நாள்',
        'result_qualifying_date': 'பொருந்தும் தகுதி தேதி',
        'result_disclaimer': 'முக்கிய அறிவிப்பு: இந்த மதிப்பீடு மக்கள் பிரதிநிதித்துவ சட்டம் 1950 பிரிவு 14(b)-ன் அடிப்படையிலான கல்வி வழிகாட்டியாகும். வயது தகுதி பெறுவது மட்டுமே வாக்காளர் பட்டியலில் சேர்க்கப்படுவதற்கான உத்தரவாதம் அல்ல. நீங்கள் அதிகாரப்பூர்வ ECI தளத்தில் படிவம் 6 சமர்ப்பிக்க வேண்டும்.',
        'result_btn_guide': 'பதிவு வழிகாட்டிக்குச் செல்லவும் (படிவம் 6)',
        'result_btn_recheck': 'வேறொரு பிறந்த தேதியை சரிபார்க்க',

        # Guide
        'guide_title': 'முழுமையான வாக்காளர் பதிவு வழிகாட்டி',
        'guide_subtitle': 'முதல்முறை வாக்காளர்கள் படிவம் 6-ஐ வெற்றிகரமாக சமர்ப்பிக்க தேவையான அனைத்து தகவல்களும்.',
        'guide_official_banner': 'விண்ணப்பங்களை இந்திய தேர்தல் ஆணையத்தின் அதிகாரப்பூர்வ இணையதளமான voters.eci.gov.in மூலம் மட்டுமே சமர்ப்பிக்க வேண்டும்.',
        'doc_checklist_title': 'ஆவணங்கள் சரிபார்ப்புப் பட்டியல்',
        'doc_checklist_desc': 'ஆன்லைன் விண்ணப்பத்தை தொடங்குவதற்கு முன் உங்களிடம் உள்ள ஆவணங்களை சரிபார்க்கவும்:',
        'doc_age_heading': '1. வயது சான்று (அங்கீகரிக்கப்பட்ட ஏதேனும் ஒரு ஆவணம்)',
        'doc_res_heading': '2. சாதாரண இருப்பிட சான்று (அங்கீகரிக்கப்பட்ட ஏதேனும் ஒரு ஆவணம்)',
        'doc_photo_heading': '3. சமீபத்திய பாஸ்போர்ட் அளவு வண்ண புகைப்படம் (அதிகபட்சம் 2MB, வெள்ளை பின்னணி)',

        # Official Services
        'services_title': 'அங்கீகரிக்கப்பட்ட தேர்தல் சேவைகள்',
        'services_subtitle': 'இந்திய தேர்தல் ஆணையம் மற்றும் மாநில தேர்தல் அமைப்புகளுக்கான நேரடி இணைப்புகள்.',
        'services_notice': 'கீழே உள்ள அனைத்து இணைப்புகளும் அதிகாரப்பூர்வ அரசு தளங்களுக்கு (*.gov.in, *.nic.in) இட்டுச் செல்கின்றன. இத்தளம் எந்தவொரு அரசு செயல்பாட்டையும் போலியாக செய்யாது.',

        # Check Registration Status
        'check_title': 'வாக்காளர் பட்டியலில் பெயர் உள்ளதா என சரிபார்ப்பது எப்படி?',
        'check_subtitle': 'தேர்தல் நாளுக்கு முன் உங்கள் பெயர் அதிகாரப்பூர்வ பட்டியலில் உள்ளதை உறுதி செய்து கொள்ளுங்கள்.',
        'check_methods_title': 'வாக்காளர் பட்டியலை தேடுவதற்கான 3 வழிகள்',
        'check_method1_title': 'வழி 1: விவரங்கள் மூலம் தேடுதல்',
        'check_method1_desc': 'பெயர், தந்தை/கணவர் பெயர், வயது, பாலினம், மாநிலம், மாவட்டம் மற்றும் சட்டமன்றத் தொகுதி விவரங்களைக் கொண்டு தேடலாம்.',
        'check_method2_title': 'வழி 2: வாக்காளர் அட்டை எண் (EPIC) மூலம் தேடுதல்',
        'check_method2_desc': 'உங்கள் 10 இலக்க EPIC எண்ணை உள்ளிட்டு உடனடியாக வாக்குச்சாவடி விவரங்களை பெறலாம்.',
        'check_method3_title': 'வழி 3: மொபைல் எண் மூலம் தேடுதல்',
        'check_method3_desc': 'படிவம் 6-ல் பதிவு செய்யப்பட்ட மொபைல் எண்ணிற்கு வரும் SMS OTP மூலம் தேடலாம்.',
        'check_action_btn': 'அதிகாரப்பூர்வ தேர்தல் தேடல் தளத்தைத் திறக்கவும் (electoralsearch.eci.gov.in)',

        # FAQ & Awareness
        'faq_title': 'வாக்காளர் விழிப்புணர்வு மற்றும் பொதுவான கேள்விகள்',
        'faq_subtitle': 'வாக்குரிமை, தகுதி மற்றும் நடைமுறைகள் பற்றிய நம்பகமான மற்றும் தெளிவான பதில்கள்.',
        'faq_filter_all': 'அனைத்து கேள்விகளும்',
        'faq_filter_eligibility': 'தகுதி & வயது',
        'faq_filter_registration': 'பதிவு & படிவம் 6',
        'faq_filter_verification': 'பட்டியல் தேடல் & சரிபார்ப்பு',
        'faq_filter_rules': 'விதிகள் & தகுதியின்மை',
        'faq_filter_services': 'உதவி எண் & செயலிகள்',
        'faq_search_placeholder': 'கேள்விகளைத் தேட தட்டச்சு செய்யவும் (எ.கா: வயது, 18, படிவம் 6, விடுபட்ட பெயர்)...',

        # Feedback
        'feedback_title': 'பெயர் குறிப்பிடாத பொதுக் கருத்துகள்',
        'feedback_subtitle': 'இச்சேவையை மேம்படுத்த உங்கள் கருத்துக்களைப் பகிருங்கள். பெயரோ அல்லது தனிப்பட்ட விவரங்களோ சேகரிக்கப்படுவதில்லை.',
        'feedback_helpful_label': 'வாக்காளர் தகுதி மற்றும் பதிவை புரிந்து கொள்ள இந்த தளம் உதவியாக இருந்ததா?',
        'feedback_opt_yes': 'ஆம், மிகவும் பயனுள்ளதாக இருந்தது',
        'feedback_opt_somewhat': 'ஓரளவு உதவியாக இருந்தது, மேம்படுத்தலாம்',
        'feedback_opt_no': 'இல்லை, தேவையான தகவல் கிடைக்கவில்லை',
        'feedback_category_label': 'எந்த பகுதி தொடர்பான கருத்து?',
        'feedback_comment_label': 'உங்கள் ஆலோசனைகள் அல்லது கருத்துகள் (விருப்பத்தின்படி)',
        'feedback_submit': 'கருத்தை சமர்ப்பிக்கவும்',

        # Footer
        'footer_about_title': 'ஸ்மார்ட் வாக்காளர் தளம்',
        'footer_about_desc': 'இந்தியாவில் உள்ள முதல்முறை வாக்காளர்கள் மற்றும் இளைஞர்களுக்கு விழிப்புணர்வை ஏற்படுத்த உருவாக்கப்பட்ட ஒரு சுயாதீன பொதுக்கல்வி தளம்.',
        'footer_quick_links': 'விரைவு இணைப்புகள்',
        'footer_official_links': 'அதிகாரப்பூர்வ தளங்கள்',
        'footer_disclaimer_title': 'சட்டப்பூர்வ பொறுப்புத்துறப்பு',
        'footer_disclaimer_text': 'பொறுப்புத்துறப்பு: இந்த தளம் ஒரு பொது விழிப்புணர்வு மற்றும் கல்வி சார்ந்த முயற்சியாகும். இது இந்திய தேர்தல் ஆணையத்தால் (ECI) இயக்கப்படவில்லை அல்லது எந்த அரசு நிறுவனத்துடனும் இணைக்கப்படவில்லை. இத்தளம் வாக்குச் சீட்டுகளை பதிவு செய்யவோ, வாக்காளர் அடையாள அட்டைகளை வழங்கவோ அல்லது வாக்காளர்களை நேரடியாகப் பதிவு செய்யவோ செய்யாது. அனைத்து அதிகாரப்பூர்வ பதிவுகளும் voters.eci.gov.in மற்றும் electoralsearch.eci.gov.in தளங்களில் மட்டுமே செய்யப்பட வேண்டும்.',
        'footer_copyright': 'ஸ்மார்ட் வாக்காளர் தகுதி மற்றும் பதிவு உதவி தளம். ஜனநாயக பங்கேற்புக்காக வெளியிடப்பட்டது.'
    }
}

def get_text(key: str, lang: str = 'en') -> str:
    """Retrieve translated text with fallback to English."""
    lang_dict = TRANSLATIONS.get(lang, TRANSLATIONS['en'])
    return lang_dict.get(key, TRANSLATIONS['en'].get(key, key))
