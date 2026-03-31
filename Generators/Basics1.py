# What is Generator ?
# Python generator are a simple way of creating iterators

# without generator as we know in previous class we have to write a big code for making'
# range 

# A simple example

# geneartor is a function in which there is no return statement but yield statement present
# gerataot is a special func joa kya krta hai ki woa temproraily pause kr jata hai or apna joa state hai 
# apna joa variable ka value hai woa yaad rkhta hai
# jbb aap usko dusri baar call krta hoa toa pichla wala chijo koa yaad krk agga kaam krta hai.
# where as ak normal function ak baar apna kaam khtm kr k memory sa nikl jata hai
# def gen_demo():

#     yield "first statement"
#     yield "second statement"
#     yield "third statement"

# gen=gen_demo()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# # below code will give same output as above
# for i in gen:
#     print(i)

def square(num):
    for i in range(1,num+1):
        yield i**2

sq=square(10)
print(next(sq))
print(next(sq))
print(next(sq))
print("Aab loop lgaeynga phr bhi uska aga sa print hoga")

for i in sq:
    print(i)