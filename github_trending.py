import requests
from datetime import datetime, timedelta
from pprint import *


def get_trending_repositories(top_size):
    url = 'https://api.github.com/search/repositories'
    prepare_date = 'created:>={}'.format((datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d'))
    payload = {'sort': 'stars', 'q': prepare_date, 'order': 'desc', 'per_page': top_size, 'page': '1'}
    r = requests.get(url, params=payload)
    pprint(r.json())


def get_open_issues_amount(repo_owner, repo_name):
    pass

if __name__ == '__main__':
    get_trending_repositories(2)
