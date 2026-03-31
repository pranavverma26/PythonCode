a = float(input("first number is = "))
b = float(input("second number is = "))
c = float(input("third number is = "))
d = float(input("forth number is = "))

if(a>b and a>c and a>d):
    print("a is greatest number.")
elif(b>a and b>c and b>d):
    print("b is greatest number.")
elif(c>a and c>b and c>d):
    print("c is the greatest number.")
else:
    print("d is the greatest number.")