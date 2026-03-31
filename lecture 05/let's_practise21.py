# WPA to find the factorial of first n numbers..

# Using for loop :-

n = int(input("Number = "))
p = 1
for i in range(1,n+1):
    p*=i

print("Factorial =", p)

# Using while loop :-

q = int(input("Value = "))
s = 1
p = 1
while p <= q:
    s*=p
    p+=1

print("Factorial = ", s)
