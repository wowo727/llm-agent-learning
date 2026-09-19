#file = open("hello.txt",'w',encoding = "utf-8")
#file.write("你好，学习文件操作")
#file.close()

with open("hello.txt",'w',encoding="utf-8") as file:
    file.write("你好")