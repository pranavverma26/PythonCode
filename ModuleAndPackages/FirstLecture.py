# import check
# 1. What do you mean by __name__ == '__main__'

### What is a module?

# Any file with an extention of .py is called a module in python.
# agar koi bhi python ka code independent aur khud sa woa run kr skta hai ya exist kr skta hai toa usko hum module bulata hai.

# Whenever we execute a program it's module name is `__main__` and 
# this name is stored in `__name__` variable

# def display():
#   print('hello')

# display()
# print(__name__)  # hum jbb he ya print krenga kisi bhi file mai uska output= __main__
# print(check.__name__)

# user_input=int(input("enter a number "))
# check.square(user_input)
# check.main()

# Importing a module
# But what is the need to import a module?
# For code modularity(code mange is easy due to module)
# code reusebility
# How to import a module

# Normal
# import test
# import math

# test.hello('Pranav')
# print(math.floor(4.3))

# clubbing together
# import math,random,test


# importing specific names from module
# from math import factorial,floor
# from test import hello

# print(factorial(5))
# ceil(4.8) ceil is present in math but we import only factorial,floor


# renaming modules
# import math as m
# import numpy as np
# import pandas as pd



# m.factorial(5)

# from math import factorial as f # we can also do this

# Order of execution of a module

# import sys
# for p in sys.path:
#   print(p)

# What are packages in Python
# A package in python is a directory containing similar sub packages and modules.
# package ak folder  hota hai jsma bhut sara .py file/module hota hai

# A particular directory is treated as package if it has __init__.py file in it.
# The __init__.py file may be empty or contain some initialization code related 
# to the package



# What are 3rd party packages?
# The python community creates packages and make it available for other programmers
# PyPI -> Python Package Index
# You can upload your own package
# You can also install packages from PyPI and install using pip
# pip is a package manager utility
# it is automatically installed with python