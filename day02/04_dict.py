students=[
    {"name":"张三","score":90},
    {"name":"李四","score":75},
    {"name":"王五","score":55}
]
for student in students:
    if student["score"]>=60:
        print(f"{student["name"]}：及格")
    else:
        print(f'{student["name"]}：不及格')