  # info.update(newDict)  # inserts the specified items to the dictionary
 #  koi bhi additional new dictionary pass kr skta h or koi bhi  key value pair pass kr skta h.

info ={
    "Name": "Pranav",
    "subjects" : {
        "phy" : 84,
        "chem": 69,
        "maths" : 88
    }
}
print(info)

# agar hm new dictionary k under new value dalnga toa ushi value mai changes aa jaygi koi new key generate nhi hoagi..

student_address = {"Name" : "Ashu", "City" : "Bihar", "age" : 19}
info.update(student_address)
print(info) 


