class Fraction:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    # Magic constructor
    def __str__(self):
        return "{}/{}".format(self.a,self.b)
    def __add__(self,other):
        num = (self.a*other.b + other.b*self.a)
        den = (self.b*other.b)
        return num/den 
    def __sub__(self,other):
        num = (self.a*other.b - other.b*self.a)
        den = (self.b*other.b)
        return num/den
    def __mul__(self,other):
        num = (self.a*other.a)
        den = (self.b*other.b)
        return num/den
    def __truediv__(self,other):
        num = (self.a * other.b)
        den = (self.b*other.a)
        return num/den
f1 = Fraction(1,2)
f2=Fraction(1,2)
print(f1+f2)
print(f1-f2)
print(f1*f2)
print(f1/f2)