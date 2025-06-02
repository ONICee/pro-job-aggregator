from app.scraper.scraper import get_all_jobs

def test_scraper_returns_list():
    jobs = get_all_jobs()
    assert isinstance(jobs, list)
    assert len(jobs) > 0

def test_job_format():
    jobs = get_all_jobs()
    sample = jobs[0]
    assert 'title' in sample
    assert 'company' in sample
    assert 'url' in sample
    assert 'source' in sample
