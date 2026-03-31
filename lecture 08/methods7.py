# Methods :- Methods are functions that belong to objects. In simple joa function hm class k andar lkhta h unhi koa hm methods khta h.

# Class k andar doa cheeja store hoa skti h 
# 1). Data(means attributes means kya kya properties h apka pass) jaisa car ke milage, car ka color etc. These are attributes/properties.
# 2).Methods :- Methods ka mtlb hota h aap kya kya kr skt hoa. jaisa car run kaisa hoti h,start kaisa hoti h etc joa bhi hmara functions hota h 
#              unha hm methods keh deta h.


class Student:
     college_name = "ABC college"  
     name = "annonymous"
    
     def __init__(self,name, marks):    
        self.name = name     
        self.marks = marks

     def Welcome(self):
         print("Welcome student,",self.name)

     def get_marks(self):
         return s1.marks
        
         
                  
s1 = Student("Pranav",97) 
s1.Welcome()
print(s1.get_marks())


