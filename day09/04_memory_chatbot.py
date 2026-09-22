#聊天历史本质上就是 Python 保存的一组消息
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key=os.getenv("OPENROUTER_API_KEY")

if not api_key:
    print("没有找到OPENROUTER_API_KEY")
    raise SystemExit

client=OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    timeout=60
)

messages=[
    {
        "role":"system",
        "content":"""
        你是一名大模型和Agent入门老师。
        用户是一名刚开始学习Python和AI的学生。

        请：
        1. 使用简单中文
        2. 专业术语要解释
        3. 尽量举简单例子
        4. 根据之前的聊天内容回答问题
        """
    }
]

print("="*20)
print("             多轮AI助手")
print("            输入quit退出")
print("="*20)

while True:
    question=input("\n你：")
    if question=="quit":
        print("\n聊天结束")
        break

    messages.append(
        {"role":"user",
        "content":question}
    )

    try:
        response=client.chat.completions.create(
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

       # print("\n---当前message---")
        #for message in messages:
            #print(message)
    except Exception as error:
        print("\n调用失败：")
        print(type(error).__name__)
        print(error)