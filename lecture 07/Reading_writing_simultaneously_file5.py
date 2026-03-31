f = open("D:\Coding Language\Python\lecture 02\pranav.txt","w+")

# truncate means completely wiped out.
# r+ hm read kr skta h or overwrite kr skta h existing data koa.. in this case no truncate happens.

print(f.read())

# w+ is use for truncate the file first and after that we can write something in the file and read it.

f.write("Hiiii")  # here r+ overwrite in the file.

# a+ the stream is positioned at the end of the file. means sentence k end mai kuch lkh skta h and then usko read kr skta h. and no truncate happens.

f.close()