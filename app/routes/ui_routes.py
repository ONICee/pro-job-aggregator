from flask import Blueprint, render_template, request
from app.scraper.scraper import get_all_jobs
from hashlib import md5

ui_bp = Blueprint('ui_bp', __name__)

def generate_job_id(job):
    """Generate a unique hash ID for each job using title, company, and URL."""
    base_str = f"{job['title']}{job['company']}{job['url']}"
    return md5(base_str.encode()).hexdigest()

@ui_bp.route('/')
def home():
    return render_template('index.html')

@ui_bp.route('/job/<job_id>')
def job_detail(job_id):
    jobs = get_all_jobs()
    
    for job in jobs:
        job['id'] = generate_job_id(job)
        if job['id'] == job_id:
            return render_template('job_detail.html', job=job)

    return "Job not found", 404
