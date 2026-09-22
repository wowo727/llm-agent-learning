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

messages = [
    {
        "role": "system",
        "content": "你是一名AI老师。"
    },
    {
        "role": "user",
        "content": "我叫小李"
    },
    {
        "role": "assistant",#assistant,AI以前说过的话
        "content": "你好，小李！"
    },
    {
        "role":"user",
        "content":"我叫什么?"
    }
]
response = client.chat.completions.create(
    model="dots-studio/dots-3-note-preview:free",
    messages=messages
)
print(response.choices[0].message.content)