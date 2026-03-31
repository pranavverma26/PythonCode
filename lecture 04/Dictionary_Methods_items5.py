           # 3. info.items()   :-  returns all (key,val) pairs as tuples.


info ={
    "key" : "value",
    "Name": "Pranav",
    "subjects" : {
        "phy" : 84,
        "maths" : 88,
    14 : ("a","b","c","d")
    }
}


print(info.items())    # dict_items([('key', 'value'), ('Name', 'Pranav'), ('subjects', {'phy': 84, 'maths': 88,  14: ('a', 'b', 'c', 'd')})])  

# type casting the above tuple into list :- 

print(tuple(info.items()))  # [('key', 'value'), ('Name', 'Pranav'), ('subjects', {'phy': 84, 'maths': 88, 14: ('a', 'b', 'c', 'd')})]

# no of tuples in previous output is 03. so we can also access these tuples individually.

# EXAMPLE :-

pairs = tuple(info.items())
print(pairs[1])   # ('Name', 'Pranav')