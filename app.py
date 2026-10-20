import os
import secrets
from datetime import datetime
from flask import (
    Flask, render_template, request, redirect, url_for,
    session, flash, abort, jsonify
)
from config import Config, ProductionConfig, DevelopmentConfig
from eligibility import evaluate_voter_eligibility
from database import init_db, get_faqs, save_feedback, get_feedback_count
from translations import get_text, TRANSLATIONS

app = Flask(__name__)

# Load configuration based on environment
env = os.environ.get('FLASK_ENV', 'development')
if env == 'production':
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)

# Ensure database and tables exist
with app.app_context():
    init_db()

# --- CSRF Protection Helpers ---
def get_csrf_token():
    if 'csrf_token' not in session:
        session['csrf_token'] = secrets.token_hex(32)
    return session['csrf_token']

def validate_csrf():
    if request.method in ('POST', 'PUT', 'DELETE', 'PATCH'):
        token = request.form.get('csrf_token') or request.headers.get('X-CSRF-Token')
        expected = session.get('csrf_token')
        if not expected or not token or not secrets.compare_digest(token, expected):
            abort(400, description="Invalid or missing CSRF token. Please refresh the page and try again.")

@app.before_request
def before_request_handler():
    # Set default language if not set
    if 'lang' not in session:
        session['lang'] = 'en'
    # Validate CSRF on mutating requests
    if request.method == 'POST':
        validate_csrf()

@app.after_request
def set_security_headers(response):
    for header, value in Config.SECURITY_HEADERS.items():
        response.headers[header] = value
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; "
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdnjs.cloudflare.com; "
        "font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com; "
        "script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com; "
        "img-src 'self' data: https:;"
    )
    return response

# Context processor to make translation helper and current language available globally
@app.context_processor
def inject_template_globals():
    current_lang = session.get('lang', 'en')
    return {
        't': lambda key: get_text(key, current_lang),
        'current_lang': current_lang,
        'csrf_token': get_csrf_token(),
        'current_year': datetime.now().year
    }

# --- Language Switcher Route ---
@app.route('/set-language/<lang>')
def set_language(lang):
    if lang in TRANSLATIONS:
        session['lang'] = lang
    # Redirect back to referring page if safe, else home
    referrer = request.referrer
    if referrer and request.host in referrer:
        return redirect(referrer)
    return redirect(url_for('index'))

# --- 1. Home Page ---
@app.route('/')
def index():
    current_lang = session.get('lang', 'en')
    # Fetch sample FAQs for preview
    faqs = get_faqs()[:4]
    return render_template('index.html', faqs=faqs)

# --- 2. Voter Eligibility Checker ---
@app.route('/eligibility')
def eligibility():
    return render_template('eligibility.html')

@app.route('/eligibility/check', methods=['POST'])
def check_eligibility():
    dob_str = request.form.get('dob')
    citizenship = request.form.get('citizenship') == 'yes'
    residence = request.form.get('residence') == 'yes'
    not_disqualified = request.form.get('not_disqualified') == 'yes'

    # Perform evaluation through modular eligibility service
    result = evaluate_voter_eligibility(
        dob_str=dob_str,
        citizenship=citizenship,
        residence_confirmed=residence,
        not_disqualified=not_disqualified
    )

    if not result.get('success'):
        # Client validation failed or invalid input
        return render_template(
            'eligibility.html',
            error=result.get('message'),
            form_data={
                'dob': dob_str,
                'citizenship': request.form.get('citizenship'),
                'residence': request.form.get('residence'),
                'not_disqualified': request.form.get('not_disqualified')
            }
        ), 400

    return render_template('eligibility_result.html', result=result)

# --- 3. Voter Registration Guide ---
@app.route('/registration-guide')
def registration_guide():
    return render_template('registration_guide.html')

# --- 4. Official Election Services ---
@app.route('/official-services')
def official_services():
    return render_template('official_services.html')

# --- 5. Voter Registration Status Guidance ---
@app.route('/check-registration')
def check_registration():
    return render_template('check_registration.html')

# --- 6. Voter Awareness & FAQ ---
@app.route('/faq')
def faq():
    category = request.args.get('category', 'all')
    faqs = get_faqs(category=category)
    return render_template('faq.html', faqs=faqs, current_category=category)

# --- 7. Anonymous Feedback ---
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        helpful = request.form.get('helpful', 'yes').strip()
        category = request.form.get('category', 'general').strip()
        comment = request.form.get('comment', '').strip()

        # Sanitize length to prevent spam
        if len(comment) > 1000:
            comment = comment[:1000]

        save_feedback(helpful, category, comment)
        flash('Thank you for your feedback! Your response helps us keep this civic portal useful and accessible.', 'success')
        return redirect(url_for('feedback'))

    count = get_feedback_count()
    return render_template('feedback.html', feedback_count=count)

# --- Error Handlers (No stack traces exposed) ---
@app.errorhandler(400)
def bad_request(e):
    return render_template('404.html', error_title="Invalid Request (400)", error_message=getattr(e, 'description', 'The request could not be processed.')), 400

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error_title="Page Not Found (404)", error_message="The civic resource or page you requested could not be located."), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html', error_title="Server Error (500)", error_message="A temporary error occurred while processing your request. Please try again shortly."), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
