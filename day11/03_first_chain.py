from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model=ChatOpenRouter(
    model="dots-studio/dots-3-note-preview:free"
)

prompt=ChatPromptTemplate.from_messages(
    [
        (
            "system","你是一名AI老师，请用简单中文回答。"
        ),
        (
            "human","请解释什么是{topic}。"
        )
    ]
)

chain=prompt | model #|把前一步输出交给后一步

response=chain.invoke(
    {
        "topic":"Agent"
    }
)
print(response.content)
#输入数据->Prompt Template->生成真正Prompt->Model->AI回答
#输入{"topic":"Agent"}->prompt ->System：你是一名AI老师Human：请解释什么是Agent ->model->模型生成回答