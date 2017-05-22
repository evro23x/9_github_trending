import requests
from datetime import datetime, timedelta


def get_trending_repositories(top_size):
    url = 'https://api.github.com/search/repositories'
    prepare_date = 'created:>={}'.format((datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d'))
    payload = {'sort': 'stars', 'q': prepare_date, 'order': 'desc', 'per_page': top_size, 'page': '1'}
    r = requests.get(url, params=payload)
    return r.json()['items']


def get_open_issues_amount(repo_owner, repo_name):
    url = 'https://api.github.com/repos/{}/{}/issues'.format(repo_owner, repo_name)
    r = requests.get(url)
    return len(r.json())


if __name__ == '__main__':
    list_top_github_repo = get_trending_repositories(10)
    for repo in list_top_github_repo:
        print('Name: {}'.format(repo['name']))
        print('Stars: {}'.format(repo['stargazers_count']))
        print('Issues: {}'.format(get_open_issues_amount(repo['owner']['login'], repo['name'])))
        print('Link: {}\n'.format(repo['url']))
