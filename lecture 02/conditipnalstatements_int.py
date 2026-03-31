
obtained_marks =float(input("obtained marks ->"))
if(obtained_marks>88):
    print("grade is A")
elif(obtained_marks<=88 and obtained_marks>=50):
    print("grade is C")
elif(obtained_marks<50):
    print("failed")
else:
    print("failed")



    ''''The use of float() before input() in the second case is necessary because you're expecting a numerical input (specifically a decimal number for marks).

Here's a breakdown:
Type of Input:

When you use input(), it always returns a string, regardless of what the user types.
If you want to perform numerical comparisons (like greater than or less than), you need to convert that input to a numerical type, such as float or int.
In the First Case:

In the first example where you check the text (like "I love you" or "What's up"), you're comparing strings. No conversion is needed because you're working with string values directly.
Summary:
Use float() (or int()) when you need to work with numbers.
No conversion is necessary for string comparisons.
If you have any more questions or need further clarification, feel free to ask!'''




