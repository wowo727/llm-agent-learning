import os
from http.client import responses

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key=os.getenv("OPENROUTER_API_KEY")

client=OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    timeout=60.0
)

messages=[
    {
        "role":"system",
        "content":"你是一名AI老师。"
    }
]
question = "我叫小李"

messages.append(
    {
        "role":"user",
        "content":question
    }
)

response=client.chat.completions.create(
    model="dots-studio/dots-3-note-preview:free",
    messages=messages
)
#把整个messages发给模型->得到answer
answer= response.choices[0].message.content

messages.append(
    {
        "role":"assistant",
        "content":answer
    }
)

print("AI：")
print(answer)

print("\n当前聊天历史：")
print(messages)