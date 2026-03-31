                                       # Conditional statement

# if-elif-else(syntax) Syntax means rules of programming or kish trah sa kisi ak chj koa lkha jayy.

 # Example :-  print() it is a syntax in python means shi tarika code k lkhna ka..    

# (jbb bhi hm kisi condition k basis prr kisi kaam koa krwana chta h for example agar hmari age 18+ hoa jaya tbb he hm apna license k lya apply kr paynga.)
'''if(condition):       here condition will be anything like age>=18, condition basically koi bhi aisi chj h joa true or false ki value ki return krti hoa.     
    Statement1          if statement ka under aisi koi bhi  value hoa joa true return krti hai toa phr statement1 joa h execute hoa jati h.'''
#Example:-
age = 21
name =8                                                
if(age>=18 and name<=8):                         # after that next line start with after pressing tab. In vs code we didn't need to press tab. tab means 4 space. Tab means indentation which means proper spacing.
    print("can vote and apply for license")      # Here also, in "and" logical operator if both values is true then it gives true so here both are trur therefore result is true so our statement will execute.
    print("can drink wine")
if(True): 
    print("you will dance") 
if(False):
    print("This statement will not execute because in condition result is false")



'''elif(conditional):   expanded version of 'elif' is (else if). it means  if first statement is not true  then we can check this statemennt.
    statement2'''

light = "green"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")
print("end of code")    # hm chae toa apna code k andar ktna bhi if or elif lkh skta h sequence mai. jbb bhi elif ata h toa suruat mai ak if statement lkhna he pdta h.

# differnce between if and elif is that ki if statement hamesa condition k leya check kregi and elif statement condition k lya tbb check kregi jbb if statement false result de rhi hoa.

num = 5

if(num > 2):
    print("no is greater than 2")
if(num > 3):
    print("no is greater than 3")

if(num>4):
    print("no is greater than 4")
elif(num>1):
    print("no is greater than 1") # this output will not come because "if" condition was statisfied. 

'''else:                    # else statement means agar upar saree ki sare conditions na false result da deya toa else run hoga..         
    statementN'''     



colour_shown = "orange"
if(colour_shown =="red"):
    print("output will not come")
elif(colour_shown=="green"):
    print("Again output will not came")    
else:
    print("this output will come")

age = 14
if(age>=18):
    print("you can vote")
else:
    print("you can't vote")



