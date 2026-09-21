import os
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
    messages = [
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
    answer = response.choices[0].message.content
    return answer

question = input("请输入问题：")
result = ask_llm(question)
print(result)

