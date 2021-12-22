import requests
import json

from requests.sessions import HTTPAdapter, session

url = ('http://127.0.0.1:8000/admin/login')

listtxt = 'text.txt'

password1 = 'bubba'

r = requests.Session()

with open('text.txt', 'r') as f:
    for word in f.readlines():
        passwd = word.replace('\n', '')
        data = {'username': passwd}
        respone = requests.post(url, data=data)
        json_obj = json.dumps(data)
        check = data.get('username')
        print(json_obj)
        if passwd == password1:
            print('Result {}'.format(passwd))
            break
        else:
            print('Sorry I can\'t find')




##### Created by dndus #####