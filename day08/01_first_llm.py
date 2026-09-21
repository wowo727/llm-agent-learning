import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()#Python，帮我读取 .env。

api_key = os.getenv("OPENROUTER_API_KEY") #os.gentenv()读取环境变量

if not api_key:
    print("OPENROUTER_API_KEY 没有加载成功")
    raise SystemExit

client = OpenAI(base_url="https://openrouter.ai/api/v1",
                api_key=api_key,
                timeout=60.0)
#client负责帮你和大模型服务器通信的“客户端”
try:
    response = client.chat.completions.create(
#response 大模型服务器返回给你的完整结果
        #model="qwen/qwen3.8-27b:free"
        model = "dots-studio/dots-3-note-preview:free",
        messages = [ #message 要发送给模型的聊天内容
            {
                "role":"user",
                "content":"请用非常简单的话解释什么是大语言模型"
            }
        ]
    )
    print(response.choices[0].message.content)
except Exception as error:
    print("调用失败：")
    print(type(error).__name__)
    print(error)