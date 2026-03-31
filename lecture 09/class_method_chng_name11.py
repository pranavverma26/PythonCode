# class ka name change krna ka tessra tareka :-

class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls,name):   # cls is not self here it is refering to the class..
        cls.name = name       

p1 = Person()
p1.changeName("rahul kumar")   
print(p1.name)
print(Person.name)