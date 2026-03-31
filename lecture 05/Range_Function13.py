# Range :- Range function returns a sequence of numbers , starting from 0 by default, and increaments by 1 (by default), 
           # and stops before a specified number.
#  For example :- Range of 5 then it returns 0,1,2,3,4

# range(start?,stop,step size?) here question marks denote that it is optional.
# start = 0
# step size = its basically ktna sa aap increase krna chta hoa. Here step size is by default 1..end = 5

print(range(5))
# we can also acess each index :- 
seq = range(5)

print(seq[0])
print(seq[3])

# we also write it in loop
for i in seq:  # here we can also write here range(5) instead of seq.
    print(i)

