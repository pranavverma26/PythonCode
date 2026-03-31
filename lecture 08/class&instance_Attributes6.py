# Class and Instance Attributes :- 

# Attributes(variablels) :- the data that is stored inside the class or inside the object.

# There are two types of attributes :-

# 1). Class attributes :- Joa sara ki sara objects/class k lya common hoti h. format = class.attr (here class = stuedent and attribute means variable)
# 2). Instance(object) attributes :- ya har objects k hisab sa alag hota hai.

class Student:
     college_name = "ABC college"  # class attributes: same for all objects
     name = "annonymous"
    
     def __init__(self,name, marks):    
        self.name = name     # obj attr> class attr           # instance attributes: diff for all objests
        self.marks = marks
        print(self)     
        print("adding new students in Database..")            

s1 = Student("Karan",97) 
print(s1.name, s1.marks)  

print(s1.college_name)  # print(Student.college_name) both are same.

s2 = Student("Arjun",88)   
print(s2.name,s2.marks)

print(s2.college_name)   #s1 and s2 dono object k lya same h output = ABC college

s3 = Student("Pranav",100)
print(s3.name)      # here if we write s3 then pranav print bcz obj attr > class attr but if we write the format of class attr print(Student.name) 
                                          # then output is annonymus.
# Examples of line 31 and 32 comment:-

s4 = Student("Shreya",101)
print(Student.name)




