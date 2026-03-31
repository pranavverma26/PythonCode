# Pickling

# Pickling is the process whereby a Python object hierarchy is
# converted into a byte stream, and 
# Unpickling is the inverse operation, whereby a 
# byte stream (from a binary file or bytes-like object) is converted back into an 
# object hierarchy.
import pickle
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display_info(self):
        print("Jii my name is",self.name,"and I am",self.age,"years old.")

p=Person("Pranav",20)

with open('person.pkl','wb') as f:
    pickle.dump(p,f)

# When to use pickle and when to use json
# Pickle lets the user to store data in binary format.JSON lets the user store data in a human redable text format.