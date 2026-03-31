count = 0
with open("D:\Coding Language\Python\lecture 07\Value.txt","r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
    

print(count)



