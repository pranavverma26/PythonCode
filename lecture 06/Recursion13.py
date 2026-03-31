# Recursion :- When a function calls itself repeatedly.
# In easy language, Recursion loop ka he ak khatarnak version h..
# Kuch kuch specific case mai loop k wajay recursion k help sa code lkhna easy hota h..but easy code generally hm loop sa lkhna prefer krta h..

def show(n):
    print(n)


show(5) 

# if we have to print 5,4 = n-1,3 = n-2 ,2 = n-3,1 or inn sbb koa hma agar ak he function call k through print krana hoa toa, recursion or 
# loop ka use kr skta h..

# Example of recursive function :-

def repeat(p):
    if(p == 0):   # ya joa condition hoti h jska basis pr hm return krta h ishi koa hm ""base case"" khta h.. line 16 
        return print("END")
    print(p)
    repeat(p-1)
    # print("END")
    
repeat(3)      

#  WORKING OF RECURSION..

# call stack :-jbb hm ak function k upar dusra function call krta h phr teshra function call krta h pr chautha function call krta h toa isha hm 
# call stack khta h.
# return krna ka mtlb h n = o wali layer delete hoa jaegi or hm wapas sa necha wala layer (n = 1) k andar aa jynga OR phr check kranga ki n=1 wala 
# layer mai koii kaam bacha h or nhi agar bcha h toa usha krnga (jaisa yha print end wala kaam bacha h toa usko complete krenga) and phr ush layer koa 
# delete kr ka uska necha wala layer n =2 pa jynga or same kaam  kraga...or ish trah sa call stack pura ka pura khali hoa gya means hmara program
# complete hoa gya.

