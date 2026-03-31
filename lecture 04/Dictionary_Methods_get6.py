#  info.get("key")  :-  Returns the value of key..
 # or we can write d.get("key")


info ={
    "Digits" : "value",
    "Name": "Pranav",
    "subjects" : {
        "phy" : 84,
        "maths" : 88,
    14 : ("a","b","c","d")
    }
}

print(info["Name"])  # if we write Name2 insteaad of Name then it gives error but in info.get we write Name2 instead of Name it does not give error
print(info.get("Name")) # and gives  output of none means there is any no any Name2 key present in my dictionary.