                                                        # TUPLES IN PYTHON



a = (2,1,3,8)   #tuple
print(a)
print(type(a))

print(a[2])   #output = 3
print(a[0])   #output = 2

'''tup[0]  = 5   this operation is not valid in tuple. but is is valid in list.'''

b =()     # it is an empty tuple but it is valid.
print(b)    #output is ()


b = (1)
print(type(b))   #  output is  <class 'int'>  so comma is necessary if we are writing one element under a tuple..
c = (1,)   
print(type(c))   # output is <class 'tuple'> .


d = ("hello")
print(type(d))    #output is <class 'str'>
e = ("hello",)
print(e)
print(type(e))


#  SLICING IN TUPLE....  IS SAME AS LIST.

print(a[1:3])   # output is  (1,3)