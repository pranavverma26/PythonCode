# Q) 4. Write a recursive function to calculate the sum of first n natural numbers.

def natural(n):
    if(n==0):
        return 0
    return natural(n-1) + n

sum = natural(5)

print(sum)