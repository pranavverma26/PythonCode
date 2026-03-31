# Q) 5. From a file containing numbers seprated by comma, print the count of even numbers.

with open("Numbers.txt","r") as p:
    data = p.read()
    print(data)

    num =""
    count = 0
    
    for element in range(len(data)):          #len(data) = 22
        if(data[element] == ","):     #print(range(len(data))) output = (0,22)
            if(int(num)%2 == 0):      #for element in range(len(data)):
                count += 1                 #print(element) output = 0
            print(int(num))                            #            1
            num = ""                                   #            .
        else:                                          #            .
            num += data[element]   #num = ""                        22
                            #num = num + "8"         case 1 :- if(data[0]==",")
                            #num = num + ","                      data[0] = 8 and 8 is not equal to "," so it will go to else
                            #print(num)  output = 8,               

print("Total number of even count = ",count)

# working explained in notes.



