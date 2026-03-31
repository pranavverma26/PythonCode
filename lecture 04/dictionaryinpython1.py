info ={
    "key" : "value",
    "Name": "Pranav",
    "learning" : "coding",
    "leacture" : 4,
    "leacture covered" : [1,2,3],
    14 : ("a","b","c","d")
}
print(info)        # {'key': 'value', 'Name': 'Pranav', 'learning': 'coding', 'leacture': 4, 'leacture covered': [1, 2, 3], 14: ('a', 'b', 'c', 'd')}
print(type(info))    #  <class'dict'>
print(info["learning"])  #  coding
print(info["Name"])        # Pranav
print(info[14])               #  ('a', 'b', 'c', 'd')

info["key"] = "Success"      

info[14] = "fourteen"

info["fav movies"] = ("Thor", "Avenger")

print(info) # {'key': 'Success', 'Name': 'Pranav', 'learning': 'coding', 'leacture': 4, 'leacture covered': [1, 2, 3], 14: 'fourteen', 'fav movies': ('Thor', 'Avenger')}
null_dict = {}
print(null_dict)     # later we can add also key values under this dictionary.