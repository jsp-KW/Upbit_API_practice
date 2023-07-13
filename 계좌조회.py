import jwt
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote

os.environ['UPBIT_OPEN_API_ACCESS_KEY'] = 'ACCESS KEY를 입력하세요'
os.environ['UPBIT_OPEN_API_SECRET_KEY'] = 'SECRET KEY를 입력하세요'

server_url = "https://api.upbit.com"
access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY'] 
secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']



payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
}


jwt_token = jwt.encode(payload, secret_key)
authorization = 'Bearer {}'.format(jwt_token)
headers = {
  'Authorization': authorization,
}


res = requests.get(server_url + '/v1/accounts',headers=headers)
#print(res.json())

my_list = res.json()
# for i in my_list:
#     temp = i['currency']
#     print(temp)


# for list in my_list:
#     for keys in list.keys():
#         print(keys)


coin_list =[]
for list in my_list:
    for values in list.values():
        print(values)
        coin_list.append(values)
