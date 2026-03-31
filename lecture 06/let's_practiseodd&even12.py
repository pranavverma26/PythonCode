# WAF to determine the number is odd or even.

def find(Number):
    if(Number%2==0):
        print("Even")
    elif(Number%2 == 1):
        print("odd")
    else:
        print("Niether odd nor even")
    

find(1.32)
find(5)
find(8)
