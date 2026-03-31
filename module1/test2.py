# import os

# print(os.getcwd())
# os.mkdir('test4.py')
keys = ["name","age"]
values=["Pranav",20]
j = 0
ans={}
while(j<len(keys)):
    ans[keys[j]]=values[j]
    j=j+1
print(ans)