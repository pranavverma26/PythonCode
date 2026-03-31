# working with binary file
#rb=readbinary
with open(r"C:\Users\prana\OneDrive\Pictures\krishna wallpaper - Copy.jpg",'rb') as f:
    with open(r'D:\Coding Language\Python\FileHandling\screenshot_copy.jpg','wb') as wf:
        wf.write(f.read())

with open("D:\sypnosis\checkFile.txt",'w') as f:
    f.write("Yay ! problem solved")

# with open("binaryCheck.txt",'wb') as f:
#     f.write(5)
# we can't put integer in text file or any comple data type like dict
with open(r"C:\Users\prana\OneDrive\Pictures\krishna wallpaper - Copy.jpg",'rb') as f:
    data =f.read()

with open(r"ImageInfo.jpg",'wb') as f:
    f.write(data)

s="hejbjbaaabacdea"
print(s.count('a'))