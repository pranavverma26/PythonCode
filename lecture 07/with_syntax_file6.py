# With Syntax :-

# files k andar file koa open krna ka or read krna ka pura ja process h usko lkhna ka or better syntax hota h using the with keyword

with open("D:\Coding Language\Python\lecture 02\pranav.txt","r") as f:
    data = f.read()
    print(data)

# as ka mtlb alias hota h...alias ka mtlb hota h jaisa clark kent is an alias for superman..bASICALLY BAAT HM USHI CHJ KA KR RHA H PRR usha. tmtlb hm kbhi 
# superman boal deta h or kbhi clark kent boal deta h..mtlb ya chj joa bhi vvalue return kregiusha hm alias or name da rha h f

with open("D:\Coding Language\Python\lecture 02\pranav.txt","w") as f:
    f.write("My name is Pranav Kr Verma.")