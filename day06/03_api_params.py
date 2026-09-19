from http.client import responses

import requests

url = "https://jsonplaceholder.typicode.com/comments"
params = {"PostId":1}  #把一些参数发送给服务器
responses = requests.get(url,params = params)

data = responses.json()
print(data)
print(type(data))

for comment in data:
    print(comment["email"])