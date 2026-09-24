import json
answer='''
{
    "risk_level":"high",
    "event_type":"异常登录",
    "reason":"发现异常登录行为",
    "action":"检查账号"
}
'''
def validata_result(answer):
    try:
        data = json.loads(answer)
        print("JSON解析成功")
        print(data)
    except json.JSONDecodeError as error:
        print("模型返回的不是合法JSON")
        return None

    required_fileds=[
        "risk_level",
        "event_type",
        "reason",
        "action"
    ]

    for field in required_fileds:
        if field not in data:
            print(f"缺少字段：{field}")
            return None

    allowed_level=[
        "low",
        "medium",
        "high"
    ]

    if data["risk_level"] not in allowed_level:
        print("risk_level不合法")
        return None

    return data

result=validata_result(answer)

if result:
    print("数据验证成功")
    print(result)