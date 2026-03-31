# Q 2). WAF to print the element of a list in a single line. (list is the parameter)



cities = ["Birpur","Madhepura","Supaul","Noida","Delhi"]
Heroes = ("\nFather", "Mother","Me","Thor")

cities[2] = "Madhubani"
# Heroes[2] = "I"

print(cities[0],end =",")
print(cities[1],end =",")
print(cities[2],end =",")
print(cities[3],end =",")
print(cities[4])


print(Heroes[0],Heroes[1],Heroes[2],Heroes[3], sep = ",")

def print_list(tuple):
    for item in tuple:
        print(item, end = ",")


print_list(cities)

print_list(Heroes)