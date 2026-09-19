import  os

from dotenv import  load_dotenv
load_dotenv()#加载 .env 文件。
api_key = os.getenv("MY_API_KEY")#从环境变量里面找到 MY_API_KEY 对应的值

print(api_key)
