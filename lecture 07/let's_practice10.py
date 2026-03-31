# Q) 3. Search if the word "learning" exists in the file or not.

def check_for_word():
    with open("D:\Coding Language\Python\lecture 07\practice.txt","r") as f:
        data = f.read()
    p = data.find("learning")
    if(data.find("learning") != -1):
        print("Found at ",p)
    else:
        print("Not Found")

check_for_word()






