from flask import Blueprint, jsonify, request
from app.scraper.scraper import get_all_jobs
from hashlib import md5

job_bp = Blueprint('job_bp', __name__, url_prefix='/api')

def generate_job_id(job):
    """Generate a unique hash ID for each job using title, company, and URL."""
    base_str = f"{job['title']}{job['company']}{job['url']}"
    return md5(base_str.encode()).hexdigest()

@job_bp.route('/jobs', methods=['GET'])
def get_jobs():
    all_jobs = get_all_jobs()

    # Attach unique ID to each job
    for job in all_jobs:
        job['id'] = generate_job_id(job)

    # Pagination Parameters
    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
    except ValueError:
        return jsonify({'error': 'Invalid pagination parameters'}), 400

    start = (page - 1) * limit
    end = start + limit
    paginated = all_jobs[start:end]

    return jsonify({
        'total': len(all_jobs),
        'page': page,
        'limit': limit,
        'jobs': paginated
    })
