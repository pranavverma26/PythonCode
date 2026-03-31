                                           # conditional statement good examples
# Grade students based on marks.



marks = int(input("marks = ")) 
if(marks >= 90):
    grade ="A"
elif(marks>=80 and marks<=90):
    grade = "B"
elif(marks >= 70 and marks <= 80):
    grade = "C"
else:
    grade = "D"

print("grade of the student is ",grade)   

