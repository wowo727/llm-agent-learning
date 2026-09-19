class Student:
    def __init__(self,name,score):
         self.name = name
         self.score = score

    def introduce(self):   #函数写在 class 里面。通常称作：方法 method。
        print(f"我叫{self.name}，分数是{self.score}")

    def is_pass(self):
        if self.score>=60:
            return True
        else:
            return False

student1 = Student("张三",90)
student2 = Student("王五",55)
student1.introduce()

print(student1.is_pass())
print(student2.is_pass())