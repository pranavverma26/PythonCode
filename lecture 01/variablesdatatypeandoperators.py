a=100
b=5
sum=a+b
print("a+b =",sum) 
print(a==b)#False
print(a<=b)#False
print(a<b)#False
"""print(a < b) output of this is error."""
"""print(a<b)'''False''' this is also gives error jbb hm comment koa single quote mai lkhta h..print()ke bagal mai"""
print(a>=b)#True
print(a%b)#0
print(a**b)#100000
# ASSIGNMENT OPERATOR
RS100=20
RS100+=10 #it's mean RS100 = RS100 + 10 which is equal to 30 so from now computer take RS100 = 30
print("RS100 =",RS100)#we have to use coma there otherwise erroe comes
RS100-=20 
print(RS100)
RS100*=2
RS100**=2
RS100%=400 #remiander of 400 divided by 400 = 0 (RS100 = RS100%400)
print("RS100 =" ,RS100)
#Logical operators
print(not False)#not operator gives opposite result
#applying not operator
print(not True)
print(not (a>b))#here answer have to be true but due to "not" operator answer is false
# AND OPERATOR..IF THE BOTH OPERATANTS ARE TRUE THEN ONLY IT GIVE TRUE RESULT OTHERWISE OUTPUT IS FALSE.
val1 =True
val2 =False
print("And operator =" ,val1 and val2)
print(RS100==0 and a>b)
# OR operator(IF ONE REUSLT IS TRUE THEN ITS OUTPUT IS TRUE IF BOTH ARE FALSE THEN THEN OUTPUT IS FALSE)
print("OR operataor = ", RS100 +10 ==10 or a<b)

