# Serialization and Deserialization

# serialization- process of converting python data types to JSON format
# Deserialization - process of converting JSON to python data types.

# using serialization and deserialization we can write complex data types in file

# JSON - Java script on notation. It is a kind of universal data format that is known or understand by every programming language


# Serialization
import json

# List
L=[1,2,3,4]
with open('D:\Coding Language\Python\FileHandling\demo.json','w') as f:
    json.dump(L,f)

# Dictionary

d = {
    'Name':'Pranav',
    'Age':20,
    'Gender':'Male',
    'Marks': [88,99,98,87]
}
with open('D:\Coding Language\Python\FileHandling\demo.json','w') as f:
    json.dump(d,f)

# Deserialization

with open(r"D:\Coding Language\Python\FileHandling\demo.json",'r') as f:
    d=json.load(f)
    print(d)
    print(type(d))

# tuple - in tuple if you dump it you get list. Which is the problrm here

t=(1,2,3,4,5)

with open('D:\Coding Language\Python\FileHandling\demo.json','w') as f:
    json.dump(t,f)
