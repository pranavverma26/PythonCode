# def mera_range(start,end):
#     for i in range(start,end):
#         yield i

# for i in mera_range(15,26):
    # print(i)

# this the code for making range using generator

# Generator expression

# As we know list comprehession

# L=[i**2 for i in range(1,10)]

# like that their is list comprehesion

# gen = (i**2 for i in range(1,11))

# for i in gen:
#     print(i)

# Benefits using generator

# 1) Ease of implementation
# 2) Memory efficient
# 3) Representing infinite streams

def all_even():
    n=0
    while True:
        yield n
        n+=2
# 4) Chaining Generators