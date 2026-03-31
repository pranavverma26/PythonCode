           # SET IN PYTHON :- Set is the collection of the uunordered items.
                            # Each element in the set must be unique and immutable.

# boolean , int , float, str ,tuple all of these values is possible to store in set but we can't store list,dictionary in set because they are mutable.

collection = {1,2,2,3,2,3,4,"hello", "world","hello"} # set can't print repeated values..means if in set there are 3 two's then it will print only one 2.
print(collection)
print(type(collection))
print(len(collection))  # total number of items. output = 06

# Empty Set

Group_info = {}  # it is an empty dictionary but not a empty set. syntax  of empty set.
print(type(Group_info))  # OUTPUT = <CLASS 'dict'>
empty_set = set()  # now it is an empty set.
print(type(empty_set))  # output = <class 'set'>   this is the syntax of empty set.
