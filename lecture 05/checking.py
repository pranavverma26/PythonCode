values =  (1,2,3,4,5,6,7,8,9,10)
x = int(input("NO that have to find = "))
p = 0
while p < len(values):
    if(values[p]==x):
        print("found at idx ", p)
        break
    print("finding")
    p += 1