                                              #List Method

#append

a =[77, 4 , 5 ,9]
print(a)   #output = [77,4,5,9]
a.append(11)  
print(a)          # [77,4,5,9,11]

#sort


a.sort() # in ascending order   
print(a)                            # output = [4,5,9,11,77]

a.sort(reverse= True)   # in descending order   
print(a)                                        # output = [77,11,9,5,4]
a.append(99)    
print(a)                  # output = [77,11,9,5,4,99]

#Reverse

b = [4,69,22,56,1]
b.reverse()
print(b)               # output = [1,56,22,69,4]
b.append(5)
print(b)               #output = [1,56,22,69,4,5]

#Insert

numbers = [4,5,9,52,33,65]
numbers.insert(3, 2)        
print(numbers)                       # OUTPUT = (4,5,9,2,52,33,65)

list= [2,1,3]
list.insert(1,5)
print(list)