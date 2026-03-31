# Open, Read , and Close File

# We have to open a file before reading or writing..

# f = open("File_name","mode") File_name or mode is parameters..by default python assume that we read the file if did not put any mode.

f = open("D:\Coding Language\Python\lecture 02\pranav.txt","r")

# data = f.read(5)  # here 5 referes that mujha suru k 5 letters he read krna h..

value = f.readline()  # if we have to read 1 line

# ak baar agar hmna data koa read kr liya toa next time woa dubara print nhi hoga uska bdla khali space aa jayga..

# print(data)

print(value)

# print(type(data))

f.close()

# Character             Meaning

# 'r'                 Open for reading(default)

# 'w'                 open for writing,truncating the file first
    
# 'x'                 create a new file and open it for working.

# 'a'                 open for writing, appending to the end of the file if it FileExistsError
    
# 'b'                 binary Mode

# 't'                 text mode(default)

# '+'                 open a disk file for updating(reading and writing)