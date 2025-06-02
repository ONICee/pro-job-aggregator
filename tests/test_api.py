from app import create_app

app = create_app()

def test_api_jobs():
    client = app.test_client()
    res = client.get('/api/jobs')
    assert res.status_code == 200
    data = res.get_json()
    assert 'jobs' in data
    assert isinstance(data['jobs'], list)
