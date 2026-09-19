def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

num1 = float(input("请输入第一个数字："))
num2 = float(input("请输入第二个数字："))
operation = input("请输入运算符（+ - * /）：")

if operation == '+':
    result=add(num1,num2)
elif operation == '-':
    result=sub(num1,num2)
elif operation == '*':
    result=multiply(num1,num2)
elif operation == '/':
    result=divide(num1,num2)
else:
    result = "输入错误"

print(f"计算结果：{result}")