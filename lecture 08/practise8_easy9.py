class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def cal_avg(self):
        sum = 0
        for avg in self.marks:
            sum += avg
        print("Hii,",self.name,",your avg score is:",sum/3)


s1 = Student("Pranav Kumar Verma",[88,78,69])
s1.cal_avg()  # output = Hii, Pranav Kumar Verma your avg score is: 78.33333333333333

s1.name = "Ironman"
s1.cal_avg()  # output = Hii, Ironman your avg score is: 78.33333333333333