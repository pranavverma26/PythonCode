# Class and Objects in Python :-

# Class is a blueprint for creating objects. Class ak woa blueprint h joa btata h ki objects k andar kya kya feature honi chaeya.

#Example :- agar hm ak student lekar ana wala h college k andar toa woa student k lya koan koan si information h joa hma apna lya system k andar 
# save krwani pregi.Student ka name bhi save krwana hoga, uska adress, roll no etc save krwana hoga..jitni bhi information hma save krwani prti 
# h kisi ak particular  object k lya usha hm ak class k andar lkhta h. or ushi koa hm blueprint khta h for an object.

# For example :- Hma apna college k lya ak system bna na h or college hma khta h ki hma bht sara student ki information save krni h ak toa tareka
#  h ki woa bht sara student ka information hm ak list ki form mai store kr la or dictionary k form mai etc..

# pr sbb sa practical tareka hoga ak class and object ki concept koa use krna.Sbsa phla toa hm ak blueprint define krenga yani class lkh kr define 
# krenga ki hm student k lya kya store krana chta h..class koa define krna k lya hm lkhta h class keyword and uska baad lkhta h hm class ka name.
# and generally joa hmara class ka name hota h usha hm capital letter sa hamesha start krta h.

# pr class koa hm waisa he use nhi kr skta h..class ki phr hma object bnani prti h..yha pr hm objects bnata h class ka blueprint use kr k.

# Creating object(instance\instances of class)... Joa hmari object hoti h unhi koa instance khta h programming k andar

class Student:              # line 20 and 21 is class  and 23 and 27 line is object.
    name = "Karan"

s1 = Student()
print(s1.name) 
print(Student.name) 


s2 = Student()
print(s2.name)