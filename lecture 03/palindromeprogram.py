# que 2. WAP to check if a list contains a palindrome of elements.  (palindrome means aisi cheja joa samna sa or picha sa same lgta hoa..)
                                                 # example :- "maam" "racecar"  palindromic list examples = [1,2,3,2,1] ,[1,"abc","abc",1]

R1 = input("1st number = ")
R2 = input("2nd number = ")
R3 = input("3rd number = ")


a = [R1,R2,R3]

b = a.copy()
b.reverse()

if(a==b):
    print("Palindromic list")
elif(a != b):
    print("Not palindromic list")