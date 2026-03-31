# Super Method :- 
# super() method is used to access methods of the parent class.

class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self,name):
        super().__init__("electric")
        super().start()
        self.name = name

car1 = ToyotaCar("prius")

print(car1.type)



