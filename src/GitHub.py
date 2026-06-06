import json

from src.fun import get_user_info, get_user_repos


def get_github_users(users):
    users_list = []
    for user in users:
        status, user_data = get_user_info(user)
        if not status:
            continue

        status, repositories = get_user_repos(user)
        if not status:
            continue

        result = {
            'login': user_data['login'],
            'public_repos': user_data['public_repos'],
            'repositories': repositories
        }

        users_list.append(result)

    return users_list


if __name__ == '__main__':
    users = ['Nikodim26']
    result = json.dumps(get_github_users(users), indent=4)
    print(result)
