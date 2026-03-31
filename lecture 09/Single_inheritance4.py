# inheritance :- When one class(child/derived) derives the properties & methods of another class(parent/base).
 
# Here class(child/derived) refers to the class which take the property from parent/base class.

# Here class(parent/base) refers to the class from which property was taken.

class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name



car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Harier")

print(car1.name)
print(car1.color)
car1.start()