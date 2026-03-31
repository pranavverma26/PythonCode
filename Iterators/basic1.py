# What is an iteration ?
# Iteration is general term for taking each item of something,onr after another. any time you
# use a loop, explicit or implicit, to go over a group of items, that is iteration

# # example :-
# num=[1,2,3]
# for i in num:
#     print(num)

# What is iterator ?
# An iterator is the object that allows the programmer to traverse through a sequence
# of data without having to store the entire data in the memory.
# -> iterator is the thing due to which iteration happens

# What is iterable ?
#-> Iterable is an object,which one can iterate over
#-> It generates an iterator when passed to iter() method.
# l=[1,2,3,4]
# print(type(l))
# # L is an iterable.
# type(iter(l)) # iter(l) -> iterator

# Point to remember ;-
# Every iterator has an iter function.
# Not all iterables are iterators
# example - list is iterable but not an iterator because we have to store whole list.

# Trick :-





# p=[1,2,3,4]
# # p is not an iterator
# iter_p=iter(p)
# iter_p is an iterator

# Understanding how for loop works:-

# num2=[1,2,3]

# # step 1 -> fetch the iterator 
# iter_num2=iter(num2)

# # step 2 -> next
# print(next(iter_num2))
# print(next(iter_num2))
# print(next(iter_num2))

# making our own for loop

# def mera_khudka_for_loop(iterable):
#     iterator=iter(iterable)
#     while True:
#         try:
#             print(next(iterator))
#         except StopIteration:
#             break
# a=[1,2,3,4,5,6]
# b=range(1,11)
# c=('A','B','C','D')
# e={0:"Hello",1:'Bye'}
# mera_khudka_for_loop(c)


num3=[1,2,3]
iter_object=iter(num3)

print(id(iter_object),'Address of iterator 1')

iter_object2=iter(iter_object)
print(id(iter_object),'Address of iterator 1')
