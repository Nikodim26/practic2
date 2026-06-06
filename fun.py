import requests


def get_user_info(user: str) -> tuple[bool, dict]:
    response = requests.get(f"https://api.github.com/users/{user}")
    if response.status_code != 200:
        return False, {}
    return True, response.json()


def get_user_repos(user: str) -> tuple[bool, list]:
    repo_response = requests.get(f"https://api.github.com/users/{user}/repos")
    if repo_response.status_code != 200:
        return False, []
    return True, [repo['name'] for repo in repo_response.json()]
