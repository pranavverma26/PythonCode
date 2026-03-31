# Break :- used to terminate the loop when encountered. 


p = 1
while p <= 8 :
    print("Hello Pranav")
    if(p==3):      # here if condition is for break.5
        break
    p += 1

# CONTINUE :- terminates execution in the current iteration and continues executtion of the loop with the next iteration.

i = 0
while i <= 5 :
    if(i==3):   # aisa krna sa 3 print nhi hoga kyuki jbb i == 3 hoga toa continue lkha hua h so print pa jana k badla i = 0 pa chla jayega.
        i += 1   # agar yha pa i = i + 1 nhi dalnga toa i = 3 he rhaga hamesa or continue hona k karna kuch print hoga he nhi..
        continue  # skip 
    print(i)
    i += 1
