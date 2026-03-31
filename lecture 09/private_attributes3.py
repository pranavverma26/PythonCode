class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()





p1 = Person()
# print(p1.name) This will give error because we made this attribute private.
# print(p1.__hello) This will also give error because we made this method private.

# In our mind one question will come, then why we made such type of function when we are not able to use it with the object ?
# Ans :- because this is that of function which is used internally by another person..means used inside the class. For example :-

p1.welcome()