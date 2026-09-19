import json
student = {
    "name" : "小李",
    "major":"网安",
    "grade":"研一"
}

with open("student.json",'w',encoding="utf-8") as file:
    json.dump(student,file,ensure_ascii=False) #Python → JSON 文件
with open("student.json", 'r', encoding="utf-8") as file:
    data = json.load(file)                     #JSON 文件 → Python
print(data)
print(data["name"])