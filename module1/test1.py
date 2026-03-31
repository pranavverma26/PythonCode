import sys,os
# # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from Python.module1.package1 import maths
# #from Python.Module2 import maths1
# print(maths.addition(3,4))
# print(maths.subtract(4,3))
# #print(maths1.mul(4,3))
# print(os.getcwd())
# import os

# # Create a new directory
# os.mkdir('new_directory')

# # List contents of the current directory
# print(os.listdir('.'))

# # Remove the newly created directory
# #os.rmdir('new_directory')
# #print(os.listdir('.'))

print(os.getcwd())
#os.chdir("D:\\Coding Language\\Python\\module1")

# We are in D:\\Coding Language directory

# with open('Python\\module1\\example.txt','r') as file:
#     content = file.read()
#     print(content)

# with open('Hello.txt','r') as file:  # In Coding Language directory.
#     content = file.read()
#     print(content)

# with open('Hello.txt','r') as file:
#     for line in file:
#         print(line.strip())  #strip remove the new line character.

# with open('Hello.txt','w') as file:
#     file.write('Hello World!\n')
#     file.write('This is a new line.\n')

# with open('Hello.txt','a') as file:
#     file.write("Append operation taking place!\n")

# lines = ['First line\n','Second line\n','Third line\n']

# with open('Hello.txt','a') as file:
#     file.writelines(lines)

# data = b'\x00\x01\x02\x03\x04'
# with open('Hello.bin','wb') as file:
#     file.write(data)

# with open('Hello.bin','rb') as file:
#     content = file.read()
#     print(content)
# l=0
# w=0
# c=0
# with open('quest.txt','r') as file:
#     for lines in file:
#         l = l +1
#         for words in lines.split():
#             w = w+1
#         for word in lines:
#                 for charecter in word:
#                     c = c +1
# print(l,w,c)

dir_name = "folder"
file_name = "file.txt"
full_path = os.path.join(dir_name,file_name)
os.chdir("folder")
os.rmdir("file.txt")

    