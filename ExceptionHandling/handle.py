import os
# Exception try, except block


# try:
#     a = b
# except:
#     print("The variable is not assigned.")

# try:
#     a=b
# except NameError as e:
#     print(f"{e}\n")

# try:
#     result=1/2
#     a=b
# except ZeroDivisionError as e:
#     print(e)
#     print("Please enter denominatror greater then 0")
# except Exception as e1:
#     print(e1)
#     print("Main exception got caught here")

# try:
#     num = int(input("Enter num: "))
#     result = 10/num
# except ValueError:
#     print("This is not a valid number")
# except ZeroDivisionError:
#     print("Enter denominator greter than 0")
# except Exception as ex:
#     print(ex)

# try,except,else block


# try:
#     num = int(input("Enter num: "))
#     result = 10/num
# except ValueError:
#     print("This is not a valid number")
# except ZeroDivisionError:
#     print("Enter denominator greter than 0")
# except Exception as ex:
#     print(ex)
# else:
#     print(f"The result is {result}")


# tru,except,else and finally

# try:
#     num = int(input("Enter num: "))
#     result = 10/num
# except ValueError:
#     print("This is not a valid number")
# except ZeroDivisionError:
#     print("Enter denominator greter than 0")
# except Exception as ex:
#     print(ex)
# else:
#     print(f"The result is {result}")
# finally:
#     print("Execution complete.")

print(os.getcwd())
try:
    file = open('ExceptionHandling\\Hello1.txt','r')
    content = file.read()
    a=b
    print(content)
except FileNotFoundError:
    print("This file is not present.")
except Exception as e:
    print(e)

finally:
    if 'file' in locals() or not file.closed():
        file.close()
        print('file close')

