# Q) 4. WAF to find in which line of the file does the word "learning" occur first.
        # print -1 if word not found.

def findline():
    word = "everwhere"
    data = True
    line_no = 1
    with open("D:\Coding Language\Python\lecture 07\practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print("Found in line ",line_no)
                return
            line_no += 1


    return print("-1")


findline()
