from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter

load_dotenv()

model=ChatOpenRouter(model="dots-studio/dots-3-note-preview:free")

response=model.invoke( "请用简单的话解释什么是LangChain。")
#invoke 执行一次调用
#model.invoke()“把这个问题交给模型执行一次。”
print(response.content)#只取 AI 回答正文