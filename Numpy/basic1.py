""""
What is numpy?
NumPy is the fundamental package for scientific computing in Python.
It is a Python library that provides a multidimensional array object, 
various derived objects (such as masked arrays and matrices), and an 
assortment of routines for fast operations on arrays, including mathematical, 
logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms,
basic linear algebra, basic statistical operations, random simulation and much 
more.
At the core of the NumPy package, is the ndarray object. This encapsulates 

n-dimensional arrays of homogeneous data types


Numpy Arrays Vs Python Sequences

NumPy arrays have a fixed size at creation, unlike Python lists (which can grow 
dynamically). Changing the size of an ndarray will create a new array and delete the original.

The elements in a NumPy array are all required to be of the same data type, and 
thus will be the same size in memory.

NumPy arrays facilitate advanced mathematical and other types of operations on large numbers of data. 
Typically, such operations are executed more efficiently and with less code than is possible using 
Python’s built-in sequences.

A growing plethora of scientific and mathematical Python-based packages are using NumPy arrays; though these typically support 
Python-sequence input, they convert such input to NumPy arrays prior to processing, and they often output NumPy arrays.
"""
import numpy as np
# 1-D Array
a=np.array([1,2,3])
print(type(a))
print(a)
print()
# 2-D array
b=np.array([[1,2,3],[4,5,6]])
print(b)
print()
# 3-d array
c=np.array([[[1,2],[3,4]],[[5,6],[6,7]]])
print(c)
print()
# dtype
d=np.array([1,2,3],dtype=float)
print(d)
print()
# np.arange
e=np.arange(1,11,2)
print("arange ",e)
print()
# with reshape
print(np.arange(16).reshape(8,2)) # makes an 2-d array of row =8 and column=2
print()
print(np.arange(16).reshape(4,4))
print()

# np.ones and np.zeros
print(np.ones((3,4)))
print()
print(np.zeros((3,4)))
print()

# np.random
print("Random :- ")
print(np.random.random((3,4))) # random ak class hai np k andar aur uska andar bhi hum random use kiya hai

print()
# np.linspace - ya given range mai equal distance prr point generate krta hai
print("Linspace :- ")
print(np.linspace(-10,10,10,dtype=int)) #np.linspace(lower,upper,no of items)
# default value of each is float so change them into int we have to do dtype=int

print()
# np.identity :- identity matrix woa hota hai jska diagonal element 1 hota hai and baki sbb zero
np.identity(3)

# Array Attributes
a1=np.arange(10)
a2=np.arange(12,dtype=float).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)

# ndim - tells about the dimension of array
print(a3.ndim)
print()
# shape - tells about no of rows and columns
print(a3.shape) # in 3-d first show much 2-d array it have and then no of rows and no of columns
print()

# size-tells about the no of elements
print(a3.size)
print()

# itemsize- tells about each item take how much space in the memory
print(a3.itemsize)


# dtype - tells about the datatype
print(a3.dtype)


print()


# Changing Data type

# astype
print(a3.dtype)
q=a3.astype(np.int32) # there two types of int 64 and 32
print(q.dtype)


# Array Operations

a4=np.arange(12).reshape(3,4)
a5= np.arange(12,24).reshape(3,4)


# scalar operations

# arithmetic
print(a4 ** 2) # power
# like that we do +,-,/...


# relational
print(a4 == 15)
print()
print(a4<15)


# vector operations - ya tbb hota hai jbb aap doa numpy array k upar operation perform krta hoa.
# arithmetic
print(a4+a5)
# we also do a1**a2
# whenever you divide result is float

print()
# Array Functions
a6 = np.random.random((3,3))
print(a6)
print("Round\n")
a6 = np.round(a6*100)
print(a6)

# max/min/sum/prod
print(np.max(a6))
print(np.min(a6))
print(np.sum(a6,axis=1))
print(np.prod(a6))

# for row wise max/min/sum/prod axis=1 and axis=0 for column
# axis=1 means:
# 👉 operation is performed across columns (row-wise)

# So:

# You are moving horizontally

# Result is usually one value per row

# in axis=0 you are moving vertically

print("Max min 0,1")
print(a6)
print()
print(np.max(a6,axis=0))
print(np.min(a6,axis=1))
print(np.sum(a6,axis=0))
print(np.prod(a6,axis=0))

# mean/median/std/var
print(np.mean(a6,axis=1))
print(np.median(a6,axis=1))
print(np.std(a6,axis=1))
print(np.var(a6,axis=1))
print()
# Trigonometry
print(np.sin(a1))
print()

# dot product
a7 = np.arange(12).reshape(3,4)
a8 = np.arange(12,24).reshape(4,3)
# it is applicable when column of a7 is equal to row of a8 and result is 3x3
print("Dot Prod = \n")
print(np.dot(a7,a8))
print("a7 and a8 =\n")
print(a7)
print()
print(a8)
print()

# log and exponents
print(np.exp(a7))
print()
print(np.log(a7))

print()
# round/floor/ceil

print(np.round(np.random.random((2,3))*100)) # round-it round up to nearest integer
print()
print(np.floor(np.random.random((2,3))*100)) # floor - it goes to previous integer
print()
print(np.ceil(np.random.random((2,3))*100)) # ceil - it goes to upcoming integer


print()
# Indexing and Slicing
print(a1) # 1-D array it behave like slicing in list
print(a1[0])
print(a1[-1])
print()


print(a2) # 2-D array
print(a2[2,1]) # [row,column]
print()

print(a3) # 3-D array
print(a3[1,0,1])
print()
# Slicing
print(a1[2:5]) #[start:end:step] same like list
print()
# 2-D array
print(a2[1:3,1:3])
"""a2[rowStart:rowEnd:step,columnStart:columnEnd:step]
    if you want :-
    0 3
    8 11
"""
print()
print(a2[::2,::3])

"""
    1 3 
    9 11
"""
print()
print(a2[::2,1::2])
print()
# 4 7
print(a2[1,::3])
print()


# 3-D Array
a3=np.arange(27).reshape(3,3,3)
print("3D array =\n")
print(a3)

print()
# print 1st level row and column
print(a3[0])
print()
# print only 1st and last level
print(a3[::2])
print()
# print 1st level 2nd row
print(a3[0,1,::])
print()
# print 2nd level middle column
print(a3[1,:,1])
print()

"""
    22 23
    25 26
"""
print(a3[2,1::,1::])
print()

"""
    0   2
    18  20
"""
print(a3[::2,0:1,::2])

print()
# Iterating
# 1-D array
for i in a1:
    print(i)
print()
# if we do this in 2-D each time one row will be printed
for i in a2:
    print(i)
print()
# if we do this in 3-D each time one 2-D will be printed
for i in a3:
    print(i)
print()

# To print each element we use nditer
for i in np.nditer(a3):
    print(i)
print()

# Reshaping
print(a2)
print("Its Transpose :- ")
print(np.transpose(a2)) # we can also write a2.T it will give same result
print()

# ravel - It converts any dimension array into 1-D
print(a3.ravel())
print()

# Stacking - It means joining two or more then two numpy array
# we can join it by horizontaly or vertically

# Horizontal stacking

a4 = np.arange(12).reshape(3,4)
print(a4)
print()
a5 = np.arange(12,24).reshape(3,4)
print(a5)
print()

print(np.hstack((a4,a5)))
print()
# Vertical stacking
print(np.vstack((a4,a5))) # we put array inside tuple
print()

# spliting - splting into equal parts
# Horizontal split
print(np.hsplit(a4,2)) # (array,no of split)
print()

# vertical splitting
print(a5)
print()
print(np.vsplit(a5,3)) # to split in x no of parts then the matrix row/column should be divisble by x