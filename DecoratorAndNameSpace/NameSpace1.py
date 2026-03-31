### Namespaces

# A namespace is a space that holds names(identifiers).Programmatically speaking, namespaces are dictionary of identifiers(keys) and their objects(values)

# There are 4 types of namespaces:
# - Builtin Namespace
# - Global Namespace
# - Enclosing Namespace
# - Local Namespace

### Scope and LEGB Rule

# A scope is a textual region of a Python program where a namespace is directly accessible.

# LEGB Rule

# The interpreter searches for a name from the inside out, looking in the local, 
# enclosing, global, and finally the built-in scope. If the interpreter doesn’t 
# find the name in any of these locations, then Python raises a NameError exception.

# Local and Global

#global var
a=2

# def temp():
#     #local
#     b=3
#     print(b)
# temp()
# print(a)

# # Global and Local Same name
# a=2
# def temp():
#     #local
#     a=3
#     print(a)
# temp()
# print(a)
# # python treat both a in different way.

# # Local and global -> local does not have but global has
# a=2
# def temp():
#     print(a)
# temp()
# print(a)

# #local and global -> Editing global
# # a=2
# # def temp():
# #     a+=1
# #     print(a)
# # temp()
# # print(a)
# #But we can't make changes in global variable in local namespcae we can only view it
# # We can do this with the help of global keyword
# a=2
# def temp():
#     global a
#     a+=1
#     print(a)
# temp()
# print(a)

# # global created inside local
# def temp():
#     global a
#     a=1
#     print(a)
# temp()
# print(a)

# #function parameter is local
# def temp(z):
#     print(z)
# a=5
# temp(a)
# print(a)
# # z is a local variable


# # Built-in scope
# # To see what things are inside built-in scope
# import builtins
# print(dir(builtins))

# # renaming in builtin

# l=[1,2,3]

# def ma():
#     print("hello")
# # max(L) this line will give error because builtin wala max run nhi hoga according 
# # to legb rule :- phla max koa local mai dhundega phr enclosing mai dhundega and phr 
# # global mai and then if global mai mill jeyga toa builtin mai nhi jeyga and hum dkh
# # skta hai ki global wala max koi argument nhi lea rha hai so max(L) will give error

# # Enclosing scope

# def outer():
#     def inner():
#         print("inner function")
#     inner()
#     print("inside outer")
# a=1
# outer()
# print("main program")

# nonlocal keyword
# def outer():
#   a = 1
#   def inner():
#     nonlocal a
#     a += 1
#     print('inner',a)
#   inner()
#   print('outer',a)

# outer()
# print('main program')


### Decorators

# A decorator in python is a function that receives another function as input and adds some functionality(decoration) to and it and returns it.

# This can happen only because python functions are 1st class citizens.

# There are 2 types of decorators available in python
# - `Built in decorators` like `@staticmethod`, `@classmethod`, `@abstractmethod` and `@property` etc
# - `User defined decorators` that we programmers can create according to our needs

# Python are 1st class function

# def modify(func,num):
#   return func(num)

# def square(num):
#   return num**2

# modify(square,2)


# # simple example

# def my_decorator(func):
#   def wrapper():
#     print('***********************')
#     func()
#     print('***********************')
#   return wrapper

# def hello():
#   print('hello')

# def display():
#   print('hello nitish')

# a = my_decorator(hello)
# a()

# b = my_decorator(display)
# b()

# Better syntax?
# simple example

# def my_decorator(func):
#   def wrapper():
#     print('***********************')
#     func()
#     print('***********************')
#   return wrapper

# @my_decorator # here we use decorator like that aur hama pichla code jaisa jyada likhna ka jrurat nhi pda
# def hello():
#   print('hello')

# hello()

# meaningful example of decorator
# hum ak aisa decorator bnana chta hai joa kisi bhi function ka execution time print krega

# import time

# def timer(func):
#     def wrapper(*args):
#         start=time.time()
#         func(*args)
#         print('time taken by',func.__name__,time.time()-start,'secs')
#     return wrapper

# # @timer
# def hello():
#     print('hello world')
#     time.sleep(2)

# here square function will give error because it has an input num but in decrator 
# we did not give any parameter as input

# so to handle this we write *args

# @timer
# def square(num):
#     time.sleep(1)
#     print(num**2)
# square(2)


# A Big Problem
# woa ya check krega ki apko joa input mila hai kisi function k andar uska data type shi
# hai ya nhi

def Check_data(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(*args)==data_type:
                func(*args)
            else:
                raise TypeError('Ye datatype nai chlega')
        return inner_wrapper
    return outer_wrapper

@Check_data(int)
def square(num):
    print(num**2)

square(2)


