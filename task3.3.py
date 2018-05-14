from pprint import pprint
import requests
from urllib.parse import urlencode
AUTH_URL = 'https://oauth.vk.com/authorize'

APP_ID = 6477690
auth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'status',
    'response_type': 'token',
    'v': '5.74'
}

# print('?'.join((AUTH_URL, urlencode(auth_data))))

TOKEN = '8001f95888d966516dd1cd17981a8277d19f9f8d127209cf968be11ec48da892db2a7ab64c79330da8171'

def friends_getmutual():
    print('Enter user_id')
    source_uid = input()
    print('Enter users_id to find mutual friends with them')
    target_uids = input()
    response = requests.get(
        'https://api.vk.com/method/friends.getMutual',
        params=dict(
            v='5.74',
            access_token=TOKEN,
            # source_uid=120008943,
            # target_uids=2761831
            source_uid=source_uid,
            target_uids=target_uids
        )
    )
    return response


def mutual_friends_pages_list(user_id_list):
    """return user_id, url"""
    response = requests.get(
        'https://api.vk.com/method/users.get',
        params=dict(
            v='5.74',
            access_token=TOKEN,
            # user_id=,
            user_ids=user_id_list,
        )
    )
    return response.json()


def data_prep():
    """Preparation input format for parameter user_ids in users.get method"""
    user_id_list = friends_getmutual().json()['response']
    str_list = [str(n) for n in user_id_list]
    user_id_list = ','.join(str_list)
    return user_id_list


for u_id in mutual_friends_pages_list(data_prep())['response']:
    print(u_id['id'], 'https://vk.com/id'+str(u_id['id']))