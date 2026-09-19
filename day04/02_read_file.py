with open("hello.txt",'r',encoding="utf-8") as file:
    content=file.read()
print(content)
print(type(content))