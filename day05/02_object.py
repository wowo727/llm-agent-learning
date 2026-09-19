class Student:

    def __init__(self,name,score):
        self.name = name
        self.score = score

#根据 Student 模板创建一个具体对象。
student1 = Student("张三",92)
student2 = Student("李四",75)

print(student1.name)
print(student1.score)
print(student2.name,student2.score)