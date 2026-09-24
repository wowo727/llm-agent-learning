from langchain_core.prompts import ChatPromptTemplate

prompt=ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一名AI老师，请使用简单中文回答。"
        ),
        (
            "human",
            "请向零基础学生解释什么是{topic}。"
        )
    ]
)

result = prompt.invoke(
    {
        "topic":"Agent"
    }
)

print(result)