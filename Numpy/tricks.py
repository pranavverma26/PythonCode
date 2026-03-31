import numpy as np
# np.sort
# Return a sorted copy of an array.

a = np.random.randint(1,100,15)
b = np.random.randint(1,100,24).reshape(6,4)
print(a)
print(np.sort(a))
# descending order
print(np.sort(a)[::-1])
print()


print(b)
print()
print(np.sort(b)) # this will done in ascending order and row wise
print()
print(np.sort(b,axis=0)) # column wise
print()


# np.append
# The numpy.append() appends values along the mentioned axis at the end of the array
# we can also append in 2-D array

print(np.append(a,200))
print()
print(np.append(b,np.ones((b.shape[0],1)),axis=1))

# np.concatenate
# numpy.concatenate() function concatenate a sequence of arrays along an existing axis.

# code
c = np.arange(6).reshape(2,3)
d = np.arange(6,12).reshape(2,3)
print()
print(c)
print()
print(d)

# You are moving horizontally at axis=1
# in axis=0 you are moving vertically
print()
print(np.concatenate((c,d),axis=0))
print()

print(np.concatenate((c,d),axis=1))

# np.cumsum
# numpy.cumsum() function is used when we want to compute the cumulative 
# sum of array elements over a given axis.
print()
print(a)
print(np.cumsum(a))
print()
print(b)
print()

print(np.cumsum(b,axis=1))

#If we do not give axis then it convert it into 1-D array 
print()

# np.cumprod
q = np.cumprod(a)
print(q)

# np.percentile
# numpy.percentile()function used to compute the nth percentile of the given data 
# (array elements) along the specified axis
print()
print("Percentile calculator")
print("percentile =(n/N)*100\n n = no of values below x\n N = Total count")
print(np.percentile(a,100))
print(np.percentile(a,50))

print()
# np.histogram
# Numpy has a built-in numpy.histogram() function which represents the frequency of 
# data distribution in the graphical form.

print(np.histogram(a,bins=[0,10,20,30,40,50,60,70,80,90,100])) # here bins means range like 0-10

# np.corrcoef
# Return Pearson product-moment correlation coefficients.
print()
salary = np.array([20000,40000,25000,35000,60000])
experience=np.array([1,3,2,4,2])
print(np.corrcoef(salary,experience)) # correlation varies from 1 to -1.

# if correlatin is +ve means exp bdhega to salary bhi bdhega
# if correlatin is -ve means exp bdhega to salary decrease hoga
# if correlatin is 0 means exp or salary mai koi relation nhi hai.

# np.isin :- ya multiple value ka presence check krta hai array mai
# With the help of numpy.isin() method, we can see that one array having values are 
# checked in a different numpy array having different elements with different sizes.

items=[10,61,32,11,89,72,63]
print(np.isin(a,items))
# if you want to print the items which are present in array
print(a[np.isin(a,items)])
print()

# np.flip 
# The numpy.flip() function reverses the order of array elements along 
# the specified axis, preserving the shape of the array.



# flipping is like mirror image
# 1-D flipping 
print(a)
print()
print(np.flip(a))
print()
# print(np.flip(b)) # In 2-D by default row and column wise dono sa flip hota hai.
print()
# but if we want ki..bsh row wise or column wise fliping hoa toa axis =0 form column or axis =1 for
# row krr skta hai.
print(b)
print()
print(np.flip(b,axis=0)) 

# np.put :- replace multiple ite with given numbers
# The numpy.put() function replaces specific elements of an array with given values 
# of p_array. Array indexed works on flattened array.

# this will change in original array
print()
print(a)
print()
np.put(a,[2,7],[26,27])
print(a)

# np.delete
# The numpy.delete() function returns a new array with the deletion of sub-arrays 
# along with the mentioned axis
 # this will not make changes in original array

print(np.delete(a,[0,3,6])) # this will delete first item
print(a)


# Set functions
# np.union1d
# np.intersect1d
# np.setdiff1d
# np.setxor1d
# np.in1d
print()
m = np.array([1,2,3,4,5])
n = np.array([3,4,5,6,7])
print("m =",m)
print("n =",n)
print("Union",np.union1d(m,n))
print("Intersection",np.intersect1d(m,n))
print("Difference",np.setdiff1d(n,m))
print("XOR",np.setxor1d(m,n)) # dono k common koa hta dega aur joa bachega usko rkh lega
print("Presence",np.in1d(m,1))
print()

# np.clip
# numpy.clip() function is used to Clip (limit) the values in an array.
print(a)
print(np.clip(a,a_min=25,a_max=75))
print(a)