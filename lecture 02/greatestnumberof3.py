# WAP to find the greatest of 3 numbers entered by the user.

a = int(input("1st number = "))
b = int(input("2nd number = "))
c = int(input("3rd number = "))

if(a>b and a>c):
    print("a is greatest number.")
elif(b>a and b>c):
    print("b is greatest number.")
else:
    print("c is greatest number.")

