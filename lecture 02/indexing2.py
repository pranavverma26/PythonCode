'''Indexing''' 

# (indexing means jbb bhi ak string create hoti h python k andar toa internally strings k sara character koa ak index/position number mill jata h)

# Apna_College ("""spaces between characters also get index""") 
# 0 1 2 3 4 5 6 7 8 9 10 11 (here 'A' got the index of 0 and so on) 
# index means to access chaaracters means agar hm chata h ki position 2 wala charac hma mill jaya toa usha hm directly acess kr skta h 
# Example :-
str = "Apna_College"
 # str[0] is 'A',str[1] is 'p' ...
ch = str[1]

print(ch) # otput 'p'
print(str[5]) #output 'c' because we start giving postion  from 0.

"""str[0] = 'B'""" #not allowed here it means replacing 'a' with 'b' gives error in indexing
# we cannot change our characters with the help of index. Means if we want to change empty spaces in str1 to any thing like @ we cannot do that.
# (str[4] = "@") this gives error as of point 15 mention. 

''' IN INDEX FORM WE CAN ONLY ACCESS CHARACTERS BUT NOT MODIFY THEM'''

 