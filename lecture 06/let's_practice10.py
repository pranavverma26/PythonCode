# Q) 3. WAF to find the factorial of n. (n is the parameter)

def cal_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
    return fact

cal_factorial(5)
cal_factorial(6)