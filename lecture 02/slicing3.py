# '''SCLICING'''

# # strings koa part mai torna koa/tukra krna koa "SLICING" khta h
# '''str[starting_idx:ending_idx]  (ending idx is not included)
# #Example :-'''

# str ="Apna college"
# print(str[2:len(str)])
# print(str[1:12])
# print(len(str))
# print(str[1:4]) 
# # output is "pna"

# print(str[:6]) # start giving position from zero. 
# # is same as str[0:6]
# print(str[3:]) 
# # is same as str[3:len(str)]   
# #IMPORTANT:- FOR 11TH INDEX WE HAVE COUNT TO 12

# print(str[5:11]) # its output is olleg
# print(str[5:12]) # its output is college



'''SLICING (NEGATIVE INDEX)'''  #SPECIAL CASE

# str1 = "Apple"
# # -5 -4 -3 -2 -1

# print(str1[-3:-1]) # output is pl in  output e is not included because we know that ending_idx is not included.
# print(str1[::len(str1)],"Hello")
# print(str1[::-1])
# print(str1[-1:-6]) # if step is positive then start<end s[start:end:step]
#  # if step is negative start>end

# p ="Pranav"
# p[0]="a"
# print(p)

t=(1,4,5)
p=(6,7)
print(type(t))
print(t.__add__(p))
#print(p)
# t[0]=p;
print(t)