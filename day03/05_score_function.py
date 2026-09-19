def get_level(score):
    if score >= 90:
        return"优秀"
    elif score >= 80:
        return "良好"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"

students=[
    {"name":"张三","score":90},
    {"name":"李四","score":75},
    {"name":"王五","score":55},
    {"name":"赵六","score":85}
]

for student in students:
    level = get_level(student["score"])

    print(
        f'姓名：{student["name"]}'
        f'成绩：{student["score"]}'
        f'等级：{level}'
    )