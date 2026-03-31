                                                    # lists in python

# A built-in data type that stores set of values.


'''marks2 = 85.1
 marks3 = 65.24
 marks4 = 58.7
 marks5 = 88.2

agar inhi marks koa hmko list k undar store krana hota toa simply hm aisa lkhta single variable bna k :-'''

marks = [65.3,85.1,65.24,58.7,88.2]

print(marks)
print(type(marks)) # output is <class 'list'>.


print(marks[0])      # It means this syntax give returs of zeroth index. so output is 65.3
print(marks[1])      # output = 85.1
print(len(marks))


marks1 = str(65.3)  # output is 4 because 6,5,.,3  len() function is used to determine the length of an object  like a str,list, or tuple.so for the programme to learn we have to put str function on them.
print(len(marks1))

'''lists in python can only store elements of different types(integer,float,string,etc..)'''


student =["Shreya", 99.6 ,"Bihar"]
print(student)

# very imortant point :- ((((((lists are mutable( it means aisi chj jo change kr skti h) in python and strings are immutable(it means aisi chj jo change nhi hoa skti h) in python))))))  

# jaisa strings k andar index pa value koa access krna allowed tha pr waha pa value koa mutated nhi kr skta tha...pr list mai hm dono kaam kr skta h..
# Example :-
school_name ="sps public school"
print(school_name[5])  #here output gives u.# string wala mai hm word deta tha or woa postion batat tha  parr ishma hm position dalta h or ya word btatta h but in slicing  we get words by writng number in print(school_name[1:3])
# school_name[5] = "a"  iish operation koa python allow nhi kr skta h because python is immutable but ya list mai hoa skta h..  


# Example :-  #student = ["Karan",85,"Delhi"]    #student[0],student[1]..
# student[0] = "Arjun"    #allowed in python
# len(student)             # returns length

address = ["Kumar chowk", "ward no = 05" ,"Birpur" ]
print(address)
print(address[2])
address[2] = "Supaul"                            #this progrrame will work in list but not in strings.
print(address)


