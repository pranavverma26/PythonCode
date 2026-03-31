# def pass_check(pass1):
#     lst1=["@","_","1","2","3","4","5","6","7","8","9"]

#     if pass1[0:1].isupper:
#         lst2 = str(lst1)
#         if( lst2 in pass1):
#             print("Strong password")
#         else:
#             print("Weak Password")

# pass_check("Ashu@90")

def shoping_cart(**cart):
    Total_Value=0
    for value in cart.values():
        value+=value
    return value
cost = shoping_cart(Copy=200,Pen=40,Sheet=56)
print(cost)






