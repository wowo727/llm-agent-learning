from asyncio import timeout

import  requests

def get_todo(todo_id):
    url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"

    try:
        response = requests.get(url,timeout=10)
        if response.status_code ==200:
            data = response.json()
            return data
        else:
            return None
    except requests.RequestException as error:
        print(f"网络错误：{error}")
        return None

todo = get_todo(1)

if todo:
    print("获取任务成功")
    print(f"ID:{todo["id"]}")
else:
    print("获取任务失败")