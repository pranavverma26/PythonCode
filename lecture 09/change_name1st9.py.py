# Class Method :-
# A class method is bound to the class & receives the class as an implicit first argument. 

# Note :- Static method can"t access or modify class state & generally for utility.

class Person:
    name = "anonymous"

    def changeName(self,name):
        Person.name = name        # class ka name change krna ka ak tareka h self k jagah yha class ka name lkh denga.

p1 = Person()
p1.changeName("rahul kumar")   # ya ak new he name create kr rha h. yha class attribute ki baat nhi hoa rhi h.pr hma ya nhi krna hma toa class attribute koa change krna h.
print(p1.name)
print(Person.name)