import json
students = [
    {"name": "张三", "score": 92},
    {"name": "李四", "score": 75},
    {"name": "王五", "score": 55},
    {"name": "赵六", "score": 85}
]
#把它保存成 JSON：
with open("student.json",'w',encoding="utf-8") as file:
    json.dump(students,file,ensure_ascii=False,indent=4)
#然后重新读取：
try:
    with open("student.json",'r',encoding="utf-8") as file:
         data=json.load(file)
    for stu in data:
        print(f"姓名：{stu["name"]}，" f"成绩：{stu["score"]}")
except FileNotFoundError:
    print("没有找到学生数据")