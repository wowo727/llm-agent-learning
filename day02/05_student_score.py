students=[
    {"name":"张三","score":90},
    {"name":"李四","score":75},
    {"name":"王五","score":55},
    {"name":"赵六","score":85}
]

print("=====学生信息管理系统=====")
for student in students:
    if student["score"]>=90:
        level="优秀"
    elif student["score"]>=80:
        level="良好"
    elif student["score"]>=60:
        level="及格"
    else:
        level="不及格"

    print(f'姓名：{student["name"]}'
    f'成绩：{student["score"]}'
    f'等级：{level}'
    )