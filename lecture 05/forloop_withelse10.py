    # Else ka use krna ka mtlb hota h for example ki hmna loop k under koi kaam kiya agar hm chate h jaisa  he loop khtm hoa jaya uska baad kuch kaam hona chaeya or
    # ,kuch chj apko print krwana hoa toa woa sara kaam hm ak optional else k under kr skta h.


str = "apnacollege"
for char in str :
    print(char)
else:
    print("End") # ya krna k baad hma ak question aa skta h ki mujha ish else ki jrurat kyu pdaa for example ish print koa bina else k jaisa
                                                                                       # str = "apnacollege"
                                                                                       #for char in str :
                                                                                       #    print(char)
                                                                                       #print("END")   Ya syntax bhi hma same output deta toa phr else ki kya jrurat padea.
                                                                                       # so hma else ki jrurat unn specific case mai padd skti h jaha hm break koa use krta h.
# Example :- use of else.
# apni str k under mujha search krna h ki mera character o kha pa ata h.. so hm aisa syntax lkhnga.
i = "AEROSPACE"
for space in i :
    if(space == "O") :
        print(" O found")
        break
    print(space)
else:
    print("END")  #else tbb print krawata jbb pura kam khtm hota lekin yha pa beach mai he o found hoa jata soa loop ruk jata h and kaam pura
                     # complete nhi hota h so else print nhi krwata h 