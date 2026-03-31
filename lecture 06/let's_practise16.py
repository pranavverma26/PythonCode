# Q) 2. Write a recursive function to print all elements in a list.

Heroes = ["Mummy","Papa","Me","Dadi","Nani","Nana"]

def element(list,idx=0):
    if(idx == len(list)):
         return
    print(list[idx])
    element(list, idx + 1 )


element(Heroes)