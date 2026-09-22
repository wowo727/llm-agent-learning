import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    timeout=60.0
)

system_message = {
    "role": "system",
    "content": "你是一名耐心的AI老师，请使用简单中文回答。"
}

messages = [
    system_message
]

while True:
    question=input("\n你：")
    if question=="quit":
        print("聊天结束")
        break

    messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    try:
        response=OpenAI.chat.completion.create(
            model="dots-studio/dots-3-note-preview:free",
            messages=messages
        )
        answer=response.choices[0].message.content

        messages.append(
            {
                "role":"assistant",
                "content":answer
            }
        )
        print(f"\nAI：{answer}")

        if len(messages)>11:
            messages=[system_message]+messages[-10]
    except Exception as error:
        print("调用失败")
        print(type(error).__name__)
        print(error)