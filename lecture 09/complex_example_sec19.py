
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):                 # by using dunder function here we can now use dunder function here.
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self,num2):                 # by using dunder function here we can now use dunder function here.
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)


num1 = Complex(1,3)
num1.showNumber()


num2 = Complex(4,6)
num2.showNumber()

# num3 = num1.add(num2)
# num3.showNumber()

# num4 = num1.add(num3)
# num4.showNumber()

# now instead of writing as line we can add complex numbers in more easy way.

num4 = num1 + num2
num4.showNumber()

num5 = num1 - num2
num5.showNumber()



