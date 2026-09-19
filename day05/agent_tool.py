from re import search
from tkinter.font import names


class Tool:
    def __init__(self,name,description):
        self.name = name
        self.description=description

    def run(self,query):
        print(f"{self.name}正在处理任务：{query}")

search_tool = Tool("搜索工具","负责搜索信息")
cal_tool = Tool("计算器","负责数学计算")

search_tool.run("搜索LangGraph是什么")
cal_tool.run("计算10+20")