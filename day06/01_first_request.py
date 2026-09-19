import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)
print(response)
print(response.status_code)
print(response.text)
#requests 发网络请求
#get 获取数据
#url 要向谁获取