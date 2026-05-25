import numpy as np
import time
import sys
# Numpy array vs Python lists

# speed :-
a= [i for i in range(10000000)]
b=[i for i in range(10000000,20000000)]
c=[]
start1 = time.time()
for i in range(len(a)):
    c=a[i]+b[i]
end1=time.time()
print("List time = ",end1-start1)
d=np.arange(10000000,dtype=np.int32)
e=np.arange(10000000,20000000)
start2 = time.time()
f=d+e
end2=time.time()
print("Numpy time = ",end2-start2)
print("Numpy faster then list = ",1.38/0.03,"times")

# So numpy is faster

# Memory :-
print("Size of a in list =",sys.getsizeof(a))
print("Size of d in narray =",sys.getsizeof(d))

# convenience :- as you see we can easily add two array in numpy.

# Advanced Indexing

a = np.arange(24).reshape(6,4)              
print(a)
print()

# Fancy Indexing


# agar ishma hmko 1st,3rd and 4th row cheya toa hum aisa kr skta hai
print(a[[0,2,3]])
print()
# if we need 1st 3rd and 4th column
print(a[:,[0,2,3]])


# Boolean Indexing

a = np.random.randint(1,100,24).reshape(6,4) # this function is used to print random int array between 1 and 100 total item =24
print()
print(a)
print()

print(a[a>50]) # print elements of array which is greater than 50.

# to print even numbers of array which greater than 50
print()

print(a[(a%2==0) & (a>50)]) # when you work with boolean value then you have to use this & not "and"



# Broadcasting
# The term broadcasting describes how NumPy treats arrays with different shapes 
# during arithmetic operations.

# The smaller array is “broadcast” across the larger array so that they have 
# compatible shapes.

# same shape
a = np.arange(6).reshape(2,3)
b = np.arange(6,12).reshape(2,3)

print(a)
print()
print(b)
print()
print(a+b)


# diff shape
a = np.arange(6).reshape(2,3)
b = np.arange(3).reshape(1,3)
print()
print(a)
print()
print(b)

print()
print(a+b)
print()


"""
Broadcasting Rules
1. Make the two arrays have the same number of dimensions.
If the numbers of dimensions of the two arrays are different, add new dimensions 
with size 1 to the head of the array with the smaller dimension.

2. Make each dimension of the two arrays the same size.
If the sizes of each dimension of the two arrays do not match, dimensions with 
size 1 are stretched to the size of the other array.

If there is a dimension whose size is not 1 in either of the two arrays, it cannot 
be broadcasted, and an error is raised.
"""

# More Examples
# 1
a = np.arange(12).reshape(4,3)
b = np.arange(3)

print(a)
print()
print(b)

print("Not error \n")
print(a+b)

# 2 :- here broadcasting is not applicable so this will give error
# a = np.arange(12).reshape(3,4)
# b = np.arange(3)

# print(a)
# print(b)

# print(a+b)

# 3
print()
print("3\n")
a = np.arange(3).reshape(1,3)
print(a)
b = np.arange(3).reshape(3,1)
print(b)
print(a+b)



# 4
a = np.arange(3).reshape(1,3)
b = np.arange(4).reshape(4,1)

print(a)
print()
print(b)
print()
print(a+b)
print()

# 5
a = np.array([1])
# shape -> (1,1)
b = np.arange(4).reshape(2,2)
# shape -> (2,2)

print(a)
print()
print(b)
print()
print(a+b)
print()

# 6 This will give error ,  broadcasting is not applicable
# a = np.arange(12).reshape(3,4)
# b = np.arange(12).reshape(4,3)

# print(a)
# print()
# print(b)
# print()
# print(a+b)
# print()

# 7 This will give error ,  broadcasting is not applicable
# a = np.arange(16).reshape(4,4)
# b = np.arange(4).reshape(2,2)

# print(a)
# print(b)

# print(a+b)

# Working with mathematical formulas

a = np.arange(10).reshape(5,2)
print(a)
print()
print(np.sum(a))
print()
print(np.sin(a))
print()

# sigmoid = 1/(1+e^-x)

def sigmoid(arr):
    return 1/(1+np.exp(-arr))

a=np.arange(100)
print(sigmoid(a))

# mean squared error

# mean squared error

actual = np.random.randint(1,50,25)
predicted = np.random.randint(1,50,25)

def mse(actual,predicted):
  return np.mean((actual - predicted)**2)

print()
print(mse(actual,predicted))

# binary cross entropy (HomeWork)




# Working with missing values

# Working with missing values -> np.nan
a = np.array([1,2,3,4,np.nan,6])
print()
print(a)

# removing missing values
print(a[~(np.isnan(a))])


# Plotting Graphs
import matplotlib.pyplot as plt

# plotting a 2D plot
# x=y
x=np.linspace(-10,10,100)
y=x
plt.plot(x,y)

# Labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Graph")

# show graph
# plt.show()

# y = x^2
x = np.linspace(-10,10,100)
y = x**2

plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
# plt.title("Y=X**2")
# plt.show()

# y = sin(x)
j = np.linspace(-10,10,100)
k = np.sin(j)

plt.plot(j,k)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("y=sin(x)")
plt.show()

