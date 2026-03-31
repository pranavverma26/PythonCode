# del keyword :- Used to delete object properties or object itself.

class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Pranav")

del s1 

# print(s1) this will give error bcz we delete the object in line 9.