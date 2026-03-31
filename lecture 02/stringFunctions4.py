                                            # string FUNCTIONS

# endswith function - returns true if string ends with substring. substr means any small string/ small part of string.

about = "i am studying python from Apnacollege."
print(len(about))
about = about.capitalize()
print(about.endswith("ege."))

#  capitalize - capitalizes 1st char

print(about.capitalize())
print(about) # hamara joa capitalize h woa ak barr work krta h  means original about k andar changes nhi krta h jbb bhi capitalize 
# kaam kr rha h toa woa ak nayi string koa create kr rha h jska andar changes honga.
# Example:- 2nd time it dosen't capitalize string

# if we want ki hamare purani string k andar bhi changes hoa toa aisa lkhna h :-

class12 = "and total no boys is thirty five "
print(class12.capitalize())
print(class12)
class12 =(class12.capitalize())
Girls = input()
print("Total no of girls in class12 is ", Girls, class12)
print("hello" ,class12)

#replaced function -replaces all occurrences of old
# string.replaced(old,new)

print(class12.replace("o","a")) # output - And tatal na bays is thirty five
print(about.replace("python","javascript"))

#Find function - returns 1st index of 1st occur

print(class12.find("b")) # output - 13 because it occurs in string in first time at 13th position.
print(about.find("python"))
print(class12.find("ram")) # output -3 because ram word is not present in class12 string.

# count function -counts the occurrence of substring.(means kisi bhi word koa pass krta h toa woa kitni baar repeat hua h usko batata h. )

print(about.count("a"))
# if we type str. then more string functions will showed.



