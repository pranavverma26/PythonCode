# case -1 If the file is not present
# f=open('Directory.txt','w')
# f.write("First Directory")
# f.write('\nHello world')
# f.write('\nHello Pranav')
# f.close()
# f.write("Hello") if we do this after close then it will give error

# case -2 If the file is present

# f = open('Directory.txt','w')
# if we write"w" on existing file then purana data overwrite hoa jata hai new data sa
# this is the problem of w mode
# f.write("Data is overwritten")
# f.close()

# f =open("D:\Coding Language\Python\FileHandling\File1.txt",'w')
# f.write("Right click on the file to get the path")
# f.close()

# The w problem is solved by append mode

# f=open("D:\Coding Language\Python\FileHandling\File1.txt",'a')
# f.write("\nKnow you see using 'a' we write inside the file without overwrtting it")
# f.close()

# what if we have to write multiple lines inside the file
# l=["\nIn one line list all things will print using writelines",'\nHi',"\nhow are you","\nI am fine"]

# f=open("D:\Coding Language\Python\FileHandling\File1.txt",'a')
# f.writelines(l)
# f.close()

# Reading from files :- use read()

# f=open("D:\Coding Language\Python\FileHandling\File1.txt",'r')
# s=f.read()
# print(s)
# f.close()
# print()

# To print n characters from the file
# f=open("D:\Coding Language\Python\FileHandling\File1.txt",'r')
# s=f.read(101)
# print(s)
# f.close()
# print()

# readline() -> to read line by line
# f=open("D:\Coding Language\Python\FileHandling\File1.txt",'r')
# print(f.readline(),end='') # due to readline and print to \n will print so we remove one therefore in print we do end=''
# print(f.readline(),end='')
# print(f.readline(),end='')
# f.close()
# print()

# reading entire using readlines

# f=open("D:\Coding Language\Python\FileHandling\File1.txt",'r')
# while True:
#     data=f.readline()
#     if data == '':
#         break
#     else:
#         print(data,end='')
# f.close()

# using context manager(With)

# its's a good idea to close a file after usage as it will free up the resources
# If we dont close it, garbage collector would close it
# with keyword closes the files as soon as the usage is over

# with open("D:\Coding Language\Python\FileHandling\File1.txt",'a') as f:
#     f.write("\nif we use with then we did not to write f.close() after doing work the file will automatically close. ")
# print("\n")
# with open("D:\Coding Language\Python\FileHandling\File1.txt",'r') as f:
#     print(f.read())
# print("\n")
# with open("D:\Coding Language\Python\FileHandling\File1.txt",'r') as f:
#     print(f.read(11))
#     print(f.read(101))
# print("\n")

# big_L =['hello world' for i in range(1000)]
# with open("D:\Coding Language\Python\FileHandling\Big.txt",'w') as f:
#     f.writelines(big_L)

# with open("D:\Coding Language\Python\FileHandling\Big.txt",'r') as f:
#     chunk_size=10
#     while len(f.read(chunk_size)) >0:
#         print(f.read(chunk_size),end='***')
#         f.read(chunk_size)

# seek and tell function
print()
with open('D:\Coding Language\Python\FileHandling\File1.txt','r') as f:
    print(f.read(10))
    print(f.tell()) # tells where is the cursor now.
    f.seek(0) # it return the cursor to 0.
    print(f.read(10))
    print(f.tell())

#seek during write

with open('D:\Coding Language\Python\FileHandling\seek.txt','w') as f:
    f.write('hello')
    f.seek(0)
    f.write('xa')

# problems with working in text mode
# can't work with binary files like images
# not good for other data types like int/float/list/tuples

