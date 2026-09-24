import json
import os
from json import JSONDecodeError

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key=os.getenv("OPENROUTER_API_KEY")

client=OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    timeout=60
)

def analyze_event(event):
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
    return response.choices[0].message.content

def validata_result(answer):
    try:
        data=json.loads(answer)
    except json.JSONDecodeError as error:
        print("模型没有返回合法JSON")
        return None

    required_fields=[
        "risk_level",
        "event_type",
        "reason",
        "action"
    ]

    for field in required_fields:
        if field not in data:
            print(f"缺少字段：{field}")
            return None

    if data["risk_level"] not in ['high','medium','low']:
        print("risk_level不合法")
        return None

    return data

event=input("请输入安全事件：")
try:
    answer=analyze_event(event)
    data=validata_result(answer)
    if data:
        print("====安全事件分析====")
        print(f"风险等级：{data["risk_level"]}")
        print(f'事件类型：{data["event_type"]}')
        print(f'判断原因：{data["reason"]}')
        print(f'处置建议：{data["action"]}')

        if data["risk_level"]=="high":
            print("该事件需要重点关注")

except JSONDecodeError as error:
    print("模型调用失败")
    print(type(error).__name__)
    print(error)