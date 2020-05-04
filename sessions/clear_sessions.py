import requests

from const import EK_CLEAR_SESSIONS


def clear_sessions():
    get = requests.get(EK_CLEAR_SESSIONS)
    print('clear_sessions(): ', get)