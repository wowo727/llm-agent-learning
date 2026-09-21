import os
from dotenv import load_dotenv
from openai import OpenAI
from pyexpat.errors import messages

load_dotenv()
api_key=os.getenv("OPENROUTER_API_KEY")
if not api_key:
    print("没有找到OPENROUTER_API_KEY")
    raise SystemExit

client=OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    timeout=60.0
)

def ask_llm(question):
    messages=[
        {
            "role": "system",
            "content": "你是一名耐心的AI老师，请用简单中文回答。"
        },
        {
            "role": "user",
            "content": question
        }
    ]
    response = client.chat.completions.create(
        model="dots-studio/dots-3-note-preview:free",
        messages=messages
    )
    return response.choices[0].message.content

print("==========================")
print("        AI 学习助手")
print("      输入 quit 退出")
print("==========================")

while True:
    question = input("请输入问题：")
    if question=="quit":
        print("\n聊天结束")
        break

    try:
        answer=ask_llm(question)
        print(f"\nAI：{answer}")
    except Exception as error:
        print("\n调用大模型失败：")
        print(type(error).__name__)
        print(error)