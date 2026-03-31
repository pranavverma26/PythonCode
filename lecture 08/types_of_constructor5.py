# Types of constructor :-

class Student:

    # Default constructors :- woa constructor jska andar sirf ak hi variable/parameter h self usha default constructor bolta h.
    def __init__(self):
        pass


    # Parameterized constructors :- woa constructor jska andar self k alawa bhi kuch parameters hota h.
    def __init__(self,name, marks):    
        self.name = name   
        self.marks = marks
        print(self)     
        print("adding new students in Database..")            

s1 = Student("Karan",97) 
print(s1.name, s1.marks)  

s2 = Student("Arjun",88)   
print(s2.name,s2.marks)

# woa constructor execute hoga joa  parameter sa match krega.  so parameterized wala execute hoga
