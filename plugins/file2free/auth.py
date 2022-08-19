import os
import requests

F2FAUTH = 'https://raw.githubusercontent.com/JAGB2021/database/blob/main/f2fauth.txt'

def auth(username):JAGB2021
    list = []
    try:
        resp = requests.get(F2FAUTH)
        text = resp.text
        list = str(text).split('\n')
    except Exception as ex:pass
    return username in list
