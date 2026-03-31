light_colour =input("colour ")  # if we write .lower() in right side of input then also it works.
#light_colour = light_colour.lower() this syntax is used if we enter the string in capital letter but condition is written in small letter then it converts automatically capital letter to small letter.
if(light_colour =="red"):
    print("stop")
elif(light_colour =="green"):
    print("go")
elif(light_colour =="yellow"):
    print("look")
else:
    print("wrong user input")