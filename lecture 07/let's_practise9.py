# Q) 2. WAF that replace all occurrences of "java" with "python" in above file.

def replace():
    with open("D:\Coding Language\Python\lecture 07\practice.txt","r") as f:
        data = f.read()

    new_data = data.replace("Java","Python")

    print(new_data)

    with open("practice.txt","w") as f:
        f.write(new_data)

replace()

