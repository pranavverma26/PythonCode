# que 01
# WAP to input user's first name and print its length

# solution:-

name = input() 
print("My name is ",name) # in name we have to type name manually because due to input function. so if we take the len of name then here this function 
print("length of name is", len(name)) 
# take the length of input that we type manually on terminal because (name= input())

# que no 2 - WAP to find the occurence of '$' in a string
# solution:- 

Money= "i earned 30000000$ and think that out of 30000000$ $ i have $ to donate $ 1000$ to a charity , 100$ for household works, and rest $ give to the parents."
print(Money.count("$"))