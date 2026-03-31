# Q) 1. Create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average.

class Student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def cal_avg(self):
        average = (self.marks1+self.marks2+self.marks3)/3
        return average


s1 = Student("Pranav Kumar Verma",88,78,69)

print("Name =",s1.name,"\nMath =",s1.marks1,"\nPhysics =",s1.marks2,"\nChemistry =",s1.marks3)

print("Hii,",s1.name,"your avg score is:",s1.cal_avg())

        