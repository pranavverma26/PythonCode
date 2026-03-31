# class ka name change krna ka dusra tareka :-

class Person:
    name = "anonymous"

    def changeName(self,name):
        self.__class__.name = "Rahul"       # __class__ = ya basically ya class person he h.

p1 = Person()
p1.changeName("rahul kumar")   
print(p1.name)
print(Person.name)