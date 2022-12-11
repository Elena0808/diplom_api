import requests
from models.data_reqres import base_url


def get_list_users(params):
    response = requests.get(f'{base_url}/api/users', params=params)
    return response


def post_create_users(name, job):
    json = {'name': name, 'job': job}
    response = requests.post(f'{base_url}/api/users', json=json)
    return response


def get_user(id_user):
    response = requests.get(f'{base_url}/api/users/{id_user}')
    return response


def update_user(id_user, name, job):
    json = {'name': name, 'job': job}
    response = requests.put(f'{base_url}/api/users/{id_user}', json=json)
    return response


def delete_user(id_user):
    response = requests.delete(f'{base_url}/api/users/{id_user}')
    return response


def post_login_user(email, password):
    json = {'email': email, 'password': password}
    response = requests.post(f'{base_url}/api/login', json=json)
    return response


def post_register_user(email):
    json = {'email': email}
    response = requests.post(f'{base_url}/api/register', json=json)
    return response
