# Q) 1. Create a new file "practice.txt" using python. Add the following data in it:
                # Hi everyone
                # We are learning File I/O
                # using Java.
                # I like programming in Java.

f = open("D:\Coding Language\Python\lecture 07\practice.txt","a+")


print(f.read())

f.write("Hi everyone\nWe are learning File I/O\nusing Java.\nI like programming in Java.")

s = open("D:\Coding Language\Python\lecture 07\practice.txt","r")

print(s.read())
