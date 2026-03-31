# Property Decorator :- We use @property decorator on any method in the class to use the method as a property.

class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem =chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"


stu1 = Student(98,97,99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.phy)  # if we again print percentage then it will not automatically change because percentage toa purana marks k hisab sa print hoa gyi.
print(stu1.percentage) # pr hm chate h jaisa he marks change hoa waisa he percentage bhi change hoa..toa aisa cases k lya jbb kisi bhi attribute koa
                           # hm fixed value nhi da skta toa uski value kisi na kisi dusra parameters k upar or kisi calculation k upar depend kregi.
# example :-
""" def calcPercentage(self):
        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

now call stu1.calcPercentage()"""   # Proper code for this is written in next file.