# Type conversion

a = 2
b = 4.25
sum = a +b

# float type is supperior then integer type

print(sum)# output 6.25. it's a float type because float is superroir then integer

'''c = "3"#here "3" is string type amd it is not added with float type. if we do the error occurs.
  To add float type and string type we have to use "Type casting"'''

# Type caststing
'''if we have to cast any value under int then we have to write :-
int(value) for int and for float,float(value)'''

c ="3"# it's type is string
c = int("3")#it's type is integer.

print(a+c)   # output = 5

a=str(a)# now type is converted from float to string.
print(type(a))
d = "4"
d = float("4")
e = 5
print(type(e+d))