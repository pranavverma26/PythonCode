# Que :- WAP to find the sum of first n natural numbers. (using while)

# sum of n natural numbers using while loop..

n = int(input("Number = "))
sum = 0
i = 0
while i <= n:
    sum += i
    i += 1

print("Total sum = ",sum)

# sum of n natural numbers using for loop..

q = int(input("Value = "))
s =0
for t in range(q + 1):
     s += t

print("Total sum ",s)
