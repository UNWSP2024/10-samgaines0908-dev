#Author: Sam Gaines
#Date: 4/2/2026
#Title: Class/ Objects

class Student:
    def check_pass_fail(self):
        if self.marks >= 78:
            return True
        else:
            return False

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

student1 = Student("Andrew",89)
student2= Student("Toby", 72)

did_pass = student1.check_pass_fail()
print(did_pass)
did_pass = student2.check_pass_fail()
print(did_pass)