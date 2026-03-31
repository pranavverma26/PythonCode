# Que no 2. Search for a number x in this tuple using a loop :
   # [1,4,9,16,25,36,49,64,81,100]

p = int(input("Number that we have to found = "))
nums =  [1,4,9,16,25,36,49,64,81,100]
idx = 0
for el in nums :
    if(el == p):
        print("NUMBER found at " , idx)
        break
    idx += 1 
else:
    print("This number is not present in the nums.")