try:
    num = int(input("请输入一个数字："))
    print(num)
except ValueError:
    print("输入错误！")

try:
    with open("abc.txt",'r',encoding="utf-8") as file:
        cotent = file.read()
    print(content)
except FileNotFoundError:
    print("文件不存在")