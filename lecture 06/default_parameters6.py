# Default Parameters :- Assigning a default value to parameter, which is used when no arguments is passed.

# Example :- we make a normal function for the multiplication of two numbers.

def multiplication(a , b):
     print(a * b)
    


multiplication(10,2)
multiplication(10,10)

# def cal_divison(d,e):
#     print(d/e)
#     return d/e

# cal_divison() without putting any parameter this function will give error so to solve this mistake we do the following thing :-

# so we have to give our parametrs a default value.

def cal_divison(d=4,e=2):
    print(d/e)
    return d/e

cal_divison()   # now this will not give error.
cal_divison(12,10)
cal_divison()