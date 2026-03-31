#     Nested Dictionary



student = {
    "Name" : "Pranav kumar verma",
    "Subjects" : {
        "physics" : 84,
        "chemistry" :69,
        "maths" : 88,
        "music" : 96,
        "English" : 71
    }
}

print(student)  # {'Name': 'Pranav kumar verma', 'Subjects': {'physics': 84, 'chemistry': 69, 'maths': 88, 'music': 96, 'English': 71}}

print(student["Subjects"])   # {'physics': 84, 'chemistry': 69, 'maths': 88, 'music': 96, 'English': 71}

print(student["Subjects"]["maths"])  # output = 88