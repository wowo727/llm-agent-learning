import requests
from requests import RequestException

url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json() #把 JSON 直接转换成 Python dict
        print("请求成功")
        print(f"任务id：{data["id"]}")
        print(f"任务内容：{data["title"]}")
        print(f"是否完成：{data["completed"]}")
    else:
        print(f"请求失败，状态码{response.status_code}")
except requests.RequestException as error:
    print(f"网络请求发生错误：{error}")

print(data)
print(type(data))