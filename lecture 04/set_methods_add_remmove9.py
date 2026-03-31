# set.add(el) :-  adds an element
# set.remove(el) :- remove the element 

# sets are mutable (means we can add or remove new elements) but the elements in sets are immutable(means we can't change the value of elements.)

collection = set() # syntax of empty set.

collection.add(1)
collection.add(2)
collection.add(2)
collection.add(3)
collection.add("Pranav")
collection.add((1,"hello",2))
# collection.add([1,2,3]) this will give error of '''unhashable type''' because list is mutable and in sets element must be immutable but set is mutable.
# Unhashable type :- joa bhi value immutable hoti h unki hash value bnn skti h hashing basically ak specific tarika/algorithim hota h jshma hm original value koa change krka kishi or chj mai convert kr deta h.
# example = aghar mera pass koi value h 1 aur dusri value bhi h 1 toa dono ki joa final hashing value ayagi woa same hogi. ishi lya python inha same chj k trah detect krta h.
# example of list :- jaisa hamara pass ak list h [1,2] or dusra list bhi h [1,2] toa dono ka same hash  value ayaga pr hm janta h ki list mutable
#  hota h toa hm dono mai sa koi bhi list mai changes kr skta h, jaisa list 2 mai hm add kr diya 3 so it become [1,2,3] now the hash value will diff from hash value of list 1
print(collection)

collection.remove(3) # if we try to remove the element which doed not exist in set then it gives error.
print(collection)

