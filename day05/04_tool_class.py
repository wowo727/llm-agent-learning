
class Tool:
    def __init__(self,name,description):
        self.name = name
        self.description = description

    def show_info(self):
        print(f"工具名称：{self.name}")
        print(f"工具描述：{self.description}")

tool1 = Tool("计算器","负责数学计算")
tool2 = Tool("搜索工具","负责搜索相关信息")

tool1.show_info()
print('-'*10)
print(tool2.show_info())