a="arul"
b="kumar"
print(a+""+b)
class stu:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
name=input("enter the name:")
age=int(input("enter the age:"))
obj=stu(name,age)
obj.display()