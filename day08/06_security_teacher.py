import os
from http.client import responses

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    timeout=60
)

def ask_llm(question):
    messages=[
        {
            "role":"system",
            "content":"你是一名网络安全老师。用户是网安专业研一学生。回答问题时优先从网络安全角度举例。"
        },
        {
            "role":"user",
            "content":question
        }
    ]
    response = client.chat.completions.create(
        model="dots-studio/dots-3-note-preview:free",
        messages=messages
    )
    return response.choices[0].message.content
print("="*10)
print("网络安全 AI 学习助手")
print("输入 quit 退出")
print("="*10)
while True:
    question=input("请输入问题：")
    if question=="quit":
        break
    try:
        answer=ask_llm(question)
        print(f"\nAI：{answer}")
    except Exception as error:
        print("调用大模型失败")
        print(type(error).__name__)
        print(error)