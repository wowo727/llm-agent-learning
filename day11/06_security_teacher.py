from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openrouter import ChatOpenRouter

load_dotenv()

concept = input("请输入网络安全概念：")
level = input("请输入你的水平：")


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            你是一名网络安全教学老师。

            学生水平：{level}

            回答要求：
            1. 先用一句话解释
            2. 再举一个生活例子
            3. 再给一个简单技术例子
            4. 最后说明基本防护思路
            """
        ),
        (
            "human",
            "请解释网络安全概念：{concept}"
        )
    ]
)


model = ChatOpenRouter(
    model="dots-studio/dots-3-note-preview:free"
)


parser = StrOutputParser()


chain = prompt | model | parser


result = chain.invoke(
    {
        "concept": concept,
        "level": level
    }
)


print("\n===== AI讲解 =====")
print(result)