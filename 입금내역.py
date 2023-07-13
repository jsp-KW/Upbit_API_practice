
import jwt
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote

os.environ['UPBIT_OPEN_API_ACCESS_KEY'] = 'ACCESS KEY를 입력해주세요'
os.environ['UPBIT_OPEN_API_SECRET_KEY'] = 'SECRET KEY를 입력해주세요'

server_url = "https://api.upbit.com"
access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY'] 
secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']

params = {
  'currency': 'KRW'
}
query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

m = hashlib.sha512()
m.update(query_string)
query_hash = m.hexdigest()

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
    'query_hash': query_hash,
    'query_hash_alg': 'SHA512',
}

jwt_token = jwt.encode(payload, secret_key)
authorization = 'Bearer {}'.format(jwt_token)
headers = {
  'Authorization': authorization,
}

res = requests.get(server_url + '/v1/deposits', params=params, headers=headers)

#print(res.json())


input_list = res.json()

total_input = 0
num =0

for i in input_list:
   
    if 'amount' in i and i['state'] =='ACCEPTED':
        print(i)
        print("\n")   

        print(str(num+1) +"번째 입금값입니다: " + i['amount'])
        num+=1

        total_input += float(i['amount'])
        print("현재 입금액 누계합은 : " + str(total_input))


print(total_input)

