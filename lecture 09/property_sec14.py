class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem =chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

    def calcPercentage(self):
        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

stu1 = Student(98,97,99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.phy)
stu1.calcPercentage()
print(stu1.percentage)

# we can do this in more simple way by using property decorator. property decorator was used in next file.
# jbb ak attribute ki value ak function k upar depend krr rhi h toa ish function koa he hm apni property bna skta h.property khna ka yha pa mtlb h 
# attribute.