import os

from dotenv import load_dotenv
from openai import OpenAI
from pyexpat.errors import messages

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    timeout=60
)
#client 用来连接和调用大模型 API 的对象

messages =[
    {
        "role":"system", #system 规定身份和规则
        "content": """
        你是一名严格的大学教授，回答要专业、简洁。
        """
    },
    {
        "role":"user", #user,提出真正的问题
        "content":"什么是大语言模型"
    }
]
response = client.chat.completions.create(
    model="dots-studio/dots-3-note-preview:free",
    messages = messages
)

answer=response.choices[0].message.content
print(answer)