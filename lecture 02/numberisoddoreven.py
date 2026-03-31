# question 01 -WAP to check if a number entered by the user is odd or even.

n = float(input("Number = "))


if(n%2 == 0 ):
    print(n, "is an even number.")
elif(n%2 == 1 ):
    print(n, "is a odd number.")
else:
    print(n," is niether even nor odd.")

