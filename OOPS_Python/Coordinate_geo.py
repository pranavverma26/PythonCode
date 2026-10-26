class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return "<{},{}>".format(self.x,self.y)
    def euclidean_distance(self,other):
        return ((self.x-other.x)**2+ (self.y-other.y)**2)**0.5
    def distance_from_origin(self):
        return self.euclidean_distance(Point(0,0))
p1=Point(2,2)
p2=Point(10,10)
print(p1)
print(p2)
x = p1.euclidean_distance(p2)
print(x)
print(p2.distance_from_origin())

class Line:
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C

    def __str__(self):
        return "{}x + {}y + {}".format(self.A,self.B,self.C)
    
    def point_on_line(p,s):
        if(p.A*s.x + p.B*s.y + p.C == 0):
            return "lies on the line"
        else:
            return "does not lie on the line" 
    def shortest_distance(self,other):
        return (self.A*other.x + self.B*other.y + self.C)/(self.A**2 + self.B**2)**0.5
    

        
l1=Line(1,1,-2)
p3=Point(1,1)
print(l1)
print(p3)
s = l1.point_on_line(p3)
print(s)
d = l1.shortest_distance(p3)
print(d)

        