 #  2.  info.values()  :-  returns all values.

info ={
    "key" : "value",
    "Name": "Pranav",
    "subjects" : {
        "phy" : 84,
        "maths" : 88,
    14 : ("a","b","c","d")
    }
}

print(info.values())   # dict_values(['value', 'Pranav', {'phy': 84, 'maths': 88,14: ('a', 'b', 'c', 'd')}])

print(list(info.values()))  # type casting the upper output into list so output =  ['value', 'Pranav', {'phy': 84, 'maths': 88,14: ('a', 'b', 'c', 'd')}]
