import requests
from bs4 import BeautifulSoup

def get_remoteok_jobs():
    jobs = []
    try:
        resp = requests.get('https://remoteok.com/remote-dev-jobs', headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(resp.text, 'html.parser')
        job_rows = soup.find_all('tr', class_='job')

        for job in job_rows:
            title = job.find('h2')
            company = job.find('h3')
            link = job.get('data-href')

            if title and company and link:
                jobs.append({
                    'title': title.text.strip(),
                    'company': company.text.strip(),
                    'source': 'RemoteOK',
                    'url': 'https://remoteok.com' + link
                })
    except Exception as e:
        print(f"[RemoteOK] Error: {e}")
    return jobs

def get_wwr_jobs():
    jobs = []
    try:
        resp = requests.get('https://weworkremotely.com/categories/remote-programming-jobs')
        soup = BeautifulSoup(resp.text, 'html.parser')
        listings = soup.find_all('li', class_='feature')

        for listing in listings:
            link_tag = listing.find('a', href=True)
            if link_tag:
                job_url = 'https://weworkremotely.com' + link_tag['href']
                company = listing.find('span', class_='company')
                title = listing.find('span', class_='title')

                if company and title:
                    jobs.append({
                        'title': title.text.strip(),
                        'company': company.text.strip(),
                        'source': 'WWR',
                        'url': job_url
                    })
    except Exception as e:
        print(f"[WWR] Error: {e}")
    return jobs

def get_remotive_jobs():
    jobs = []
    try:
        resp = requests.get('https://remotive.io/api/remote-jobs')
        data = resp.json()
        for job in data['jobs']:
            jobs.append({
                'title': job['title'],
                'company': job['company_name'],
                'source': 'Remotive',
                'url': job['url']
            })
    except Exception as e:
        print(f"[Remotive] Error: {e}")
    return jobs

def get_all_jobs():
    return get_remoteok_jobs() + get_wwr_jobs() + get_remotive_jobs()
