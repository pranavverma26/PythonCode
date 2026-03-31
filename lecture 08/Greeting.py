class Greetings:
    message = "Hello, World!"

    def say_hello(self):
        print(self.message)

print(Greetings.message)
s1 = Greetings()
s1.say_hello()
print(s1.message)