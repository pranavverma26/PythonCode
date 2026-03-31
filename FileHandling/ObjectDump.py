import json
def show_object(person):
    if isinstance(person,Person):
        # return "Name -> {},Age -> {},Gender -> {}".format(person.name,person.age,person.gender)
        return {'Name':person.name,'age':person.age,'gender':person.gender}

class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def details(self):
        print("Name =",self.name)
        print("Age =",self.age)
        print("Gender =",self.gender)
    def VoteEligible(self):
        if(self.age<18):
            print("Na munna na")
        else:
            print("Yes you are elegible to vote BJP")

p1=Person("Pranav",20,"male")
p1.details()
p1.VoteEligible()


with open("SelfObject.json",'w') as f:
    json.dump(p1,f,default=show_object,indent=4)

with open("SelfObject.json",'r') as f:
    d=json.load(f)
    print(d)
    print(type(d))
