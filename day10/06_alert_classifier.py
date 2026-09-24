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
        "category": "malware/phishing/login/network/other",
        "severity": "high",
        "summary": "事件概要",
        "need_human_review": true
    }}
    
    要求：
    category只能是：
    malware
    phishing
    login
    network
    other
    
    severity 只能是：
    low
    medium
    high
    
    need_human_review 必须是JSON布尔值：
    true或者false
    
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

def validate_result(result):
    try:
        data=json.loads(result)
    except JSONDecodeError as error:
        print("错误！没有返回合法JSON")
        return None

    required_field=["category","severity","summary","need_human_review"]
    for field in required_field:
        if field not in data:
            print(f"缺少字段{field}")
            return None

    if data["category"] not in ['malware','phishing','login','network','other']:
        print("category不合法")
        return None

    if data["severity"] not in ['low','medium','high']:
        print("severity不合法")
        return None

    if not isinstance(data["need_human_review"], bool):
        print("need_human_review必须是布尔值")
        return None

    return data

event=input("请输入安全事件：")
try:
    answer=analyze_event(event)
    data=validate_result(answer)
    print(f"模型原始回答：{answer}")
    if data:
        if data["need_human_review"]:
            print("该告警需要人工审核")
        else:
            print("该告警暂不需要人工审核")
except JSONDecodeError as error:
    print("模型调用失败")
    print(type(error).__name__)
    print(error)


