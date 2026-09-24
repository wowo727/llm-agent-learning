import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key=os.getenv("OPENROUTER_API_KEY")

client=OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    timeout=60
)

event=input("请输入安全事件：")

prompt = f"""
你是一名网络安全分析助手。
请分析下面的安全事件：
{event}

请只返回JSON，格式必须是：
{{
    "risk_level": "low/medium/high",
    "event_type": "事件类型",
    "reason": "判断原因",
    "action":"建议采取的措施"
}}

要求：
risk_level只能是：
low
medium
high

不要输出JSON以外的内容。
不要使用Markdown代码块。
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
data=json.loads(answer)

print("====安全事件分析====")
print(f"风险等级：{data["risk_level"]}")
print(f'事件类型：{data["event_type"]}')
print(f'判断原因：{data["reason"]}')
print(f'处置建议：{data["action"]}')