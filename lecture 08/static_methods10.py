# Static Methods :- Methods that don't use the self parameter(work at class level)

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks


    @staticmethod  # decrator :- This decorator converts a function to static method.
    def Hello():  # if we have to print hello then we have to use staticmethod so that line 22 will not give error and print Hello.
        print("Hello Baby")

    def cal_avg(self):
        sum = 0
        for avg in self.marks:
            sum += avg
        print("Hii,",self.name,",your avg score is:",sum/3)


s1 = Student("Pranav Kumar Verma",[88,78,69])
s1.cal_avg()  
s1.Hello()
Student.Hello()
