# Q 4). Search for a number x in this tuple using loop :
    # (1,4,9,16,25,36,49,64,81,100)

# Solution :- 

values = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Number to find : "))
i = 0
while i < len(values):
    if(values[i]==x):    # here if condition is for print.
        print("Found at idx ", i)
        break
    else:
        print("finding")
    i += 1

    # This type of searching a number is called linear search which means ak ak kr k value k upar jynga or check krenga kii ya value h or nhi this process is called linear search.