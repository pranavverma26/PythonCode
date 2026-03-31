# python k andar as such, complex number koa create krna ka koi class toa h nhi..toa hm apni khud ki class bnaynga or aisi class joa 
# complex number koa create kr ska jaisa..Integer,string,list etc class h python k andar.
# we are going to create a class called complex :-

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def add(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(1,3)
num1.showNumber()


num2 = Complex(4,6)
num2.showNumber()

num3 = num1.add(num2)
num3.showNumber()

num5 = num1.add(num3)
num5.showNumber()

