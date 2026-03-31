# Que 3. WAP to enter marks of 3 subjects from the user and store them in a dictionary.Start with an empty dictionary and 
       # Add one by one . Use subject name as key and marks as value.
# solution :-

Marks = {}
R1 = int(input("Physics Marks ="))
Marks.update({"Physics" : R1})

R2 = int(input("Chemistry Marks ="))
Marks.update({"Chemistry" : R2})

R3 = int(input("Math marks ="))
Marks.update({"Math" : R3})

print(Marks)
