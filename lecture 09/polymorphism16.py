# What we have studied in this chapter :- 
# 1). firstly we see about the four pillars off OOP. In which we learn about i) Abstraction ii) Encapsulation iii) Inheritance

# And fourth pillar is Polymorphism. now we talk about the :-


# Polymorphism : Operator Overloading

# When the same operator is allowed to have different meaning according to the context.

# Basically it means jbb ak he chj koa alag alag trah sa use kya jaya toa woa basically comes in the cateogry of Polymorphism.

# In python, Operator Overloading  is the best example of polymorphism.


print("apna" + "college")  # here it is also + operator but these are not numbers. But here work of + operator is to concatenate two strings.

# output = apnacollege

print([1,2,3] + [4,5,6]) # Here work of + operator is to merge both list.
print(type(1)) # output = <class 'int'> 

print(1 + 2) # output =3, Here operator is + operator.

# Basically Python k andar already ak class int, integer wali class exist krti h or maina koi bhi integer agar lkha woa basically ush class ka
# object hoga.

# So in line 26. 1 and 2 is a object  and because it is a integer type inka lya already ush class int k andar defined h ki + ka mtlb h doa
# numbers koa add kro.

print(type("apna")) # output = <class 'str'>

# python k andar already ak string class exist krta h jiski sari ki sari strings object h or ish class str k andar already define h ki 
# jbb bhi + likha jyga toa uska mtlb h doa strings koa add krna.

print(type([1,2,3])) # output = <class 'list'>
# Python k andar already ak list class define h jiski [1,2,3] and [4,5,6] is a object or list class k andar already ya define h kii + operator
# ka mtlb h dono list koa merge krna h.

# above this all are implicit overloading.