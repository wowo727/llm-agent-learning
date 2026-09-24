import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key=os.getenv("OPENROUTER_API_KEY")

client=OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    timeout=60
)

prompt = """
请分析下面这句话：
“我是网络安全专业的研一学生，正在学习Agent开发。”
请只返回JSON，格式必须是：
{
    "major": "专业",
    "grade": "年级",
    "learning": "正在学习的内容"
}
不要输出任何其他文字。
"""
response=client.chat.completions.create(
    model="dots-studio/dots-3-note-preview:free",
    messages=[
        {
            "role":"user",
            "content":prompt
        }
    ]
)

answer=response.choices[0].message.content

print(f"模型原始回答：{answer}")
print(f"\n模型回答的类型：{type(answer)}")

data=json.loads(answer)

print(f"转换以后：{data}")
print(f"转换以后的类型：{type(data)}")