def print_hello():
    print("hello")
    


print(print_hello())   # output = none bcz na ya koi input la rha or na he kuch parameter h, na he kuch output da rha h or na he uski kuch return value h


# another example...

# average of 3 numbers.


def cal_ave(a, b, c):
    average = (a+b+c)/3
    
    return average
    
sum = cal_ave(1,1,1)
print("NUMBER IS ",sum)
print(cal_ave(1, 2, 3))
print(cal_ave(10, 15 , 29))