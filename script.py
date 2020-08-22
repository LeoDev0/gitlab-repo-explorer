import requests
import sys


username = str(input('Quer listar repositórios de que usuário? '))
user_data_url = f'https://gitlab.com/api/v4/users/?username={username}'

get_user_data = requests.get(user_data_url)

try:
    user_id = get_user_data.json()[0]['id']
except IndexError :
    print('Usuário não existe')
    sys.exit(1)

user_projects_url = f'https://gitlab.com/api/v4/users/{user_id}/projects'
get_projects = requests.get(user_projects_url).json()

number_of_repos = len(get_projects)
if number_of_repos == 0:
    print(f'{username} não possui repositórios públicos')
else:
    print(f'{username} possui {number_of_repos} repositórios')
    print('')
    for i in get_projects:
        print(i['name'])
