from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openrouter import ChatOpenRouter

load_dotenv()

prompt=ChatPromptTemplate(
    [
        (
            "system",
            "你是一名AI老师，请简单回答。"
        ),
        (
            "human",
            "请解释什么是{topic}。"
        )
    ]
)

model=ChatOpenRouter(model="dots-studio/dots-3-note-preview:free")

parser=StrOutputParser() #把模型输出解析成字符串。

chain=prompt | model |parser #parser->变成普通str

result = chain.invoke(
    {
        "topic":"LangChain"
    }
)

print(result)
print(type(result))