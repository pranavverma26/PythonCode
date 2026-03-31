# _ _init_ _ Function

# Constructor :- it is basically the init function. ya joa function h object creation k time pa invoke(execute) hota h.

# All classes have a function called __init__(), which is always executed when the object is being initiated.

# abhi yha pr apna class k andar hmna koi init function nhi lkha h toa python kya krti h automatically  hmara lya ak
# init function create krti h or   usko execute jrur kregi

# agar constructor hma khud lkhna hoa toa hm aisa lkhnga :-
class Student:
     def __init__(self,name, marks):    # constructor k andar hm multiple parameters bhi la skta h jaisa ak parameter self(hamesha 1st parameter hota h)
        self.name = name   # self.name ka mtlb h joa object k anadr new create hona wala h.
        self.marks = marks
        print(self)    #print(self) krna sa whi print hua joa print(s1) krna sa hota h.so self means joa new object h 
        print("adding new students in Database..")               # joa create hoa rhi h ishi koa hm self kh rha h yha..s1 object koa self kh rha h.

s1 = Student("Karan",97) # output = adding new students in Database..  bina print kya hua he yha output aa jyga bcz automatically yha function call hoa jyga..
print(s1.name, s1.marks)  # output = Karan

s2 = Student("Arjun",88)   # constructor harr new object k sath ak baar call hota h.
print(s2.name,s2.marks)

# Attributes(variables = s1) :- the data that is stored inside the class or inside the object


# Note :- The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.



# aab hm notice krange ki jaisa he hm apna s1 wala object koa create krenga waisa he sbsa phla kya hoga init function sbsa phla call hojayga
# ya joa paranthesis[()] h student k bagal mai constructor koa call krna k lya lgaya jata h toa automatically init function call hoa jayga.

# Constructor hamesa ak argument leta h which is called the self parameter



