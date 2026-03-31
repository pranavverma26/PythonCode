def add(a,b):
    sum_result = a+b
    print("The sum is ", sum_result)

result = add(5,3)
print("Result: ", result) # this will print 'Result:None.'

# Now if we use return it will not give none.

def add(d,e):
    value = d + e
    print("The sum is ", value)
    return value

number = add(11,10)
print("Final Marks =", number)

print("there are several",number)