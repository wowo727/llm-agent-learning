from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openrouter import ChatOpenRouter

load_dotenv()
model = ChatOpenRouter(
    model="dots-studio/dots-3-note-preview:free"
)

prompt = ChatPromptTemplate(
    [
        (
            "system",
            """
            你是一名AI教学助手。
            根据学生情况调整解释难度。
            """
        ),
        (
            "human",
            """
            学生专业：{major}
            学生水平：{level}
 
            请解释：{topic}
            """
        )
    ]
)

chain = prompt | model
response = chain.invoke(
    {
        "major": "网络安全",
        "level": "零基础",
        #"topic": "RAG"
    }
)
print(response.content)