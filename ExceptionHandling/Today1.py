# # There are 2 stages where error may happen in a program
# # 1) During compilation -> Syntax Error
# # 2) During execution -> Exceptions

# # Syntax Error

# # Something in the program is not written according to the program grammar.
# # Error is raised by the interpreter/compiler
# # You can solve it by rectifying the program


# # IndexError
# # The IndexError is thrown when trying to access an item at an invalid index.
# # L = [1,2,3]
# # L[100] # because index 100 is not present there

# # ModuleNotFoundError
# # The ModuleNotFoundError is thrown when a module could not be found.
# # import mathi
# # math.floor(5.3)

# # KeyError
# # The KeyError is thrown when a key is not found

# # d = {'name':'nitish'}
# # d['age']


# # TypeError
# # The TypeError is thrown when an operation or function is applied to an object of an inappropriate type.
# # 1 + 'a'

# # ValueError
# # The ValueError is thrown when a function's argument is of an inappropriate type.
# # int('a')

# # NameError
# # The NameError is thrown when an object could not be found.
# # print(k)

# # AttributeError
# # L = [1,2,3]
# # L.upper() because list object does not have upper attribute

# ### Exceptions

# # If things go wrong during the execution of the program(runtime). 
# # It generally happens when something unforeseen has happened.
# # - Exceptions are raised by python runtime
# # - You have to takle is on the fly

# #### **Examples**
# # - Memory overflow
# # - Divide by 0 -> logical error
# # - Database error


# # Why is it important to handle exceptions
# # Two reason - 1) because error,user expereince koa khrab krta hai 2) security because if error happen then hacker can see what is the name of file where it is located
# # how to handle exceptions
# # -> Try except block

# # let's create a file

# with open(r"D:\Coding Language\Python\ExceptionHandling\Hello1.txt",'w') as f:
#     f.write("Hello World")

# # try cath demo

# try:
#     with open(r"D:\Coding Language\Python\ExceptionHandling\Hello.txt",'r') as f:
#         print(f.read())
# except:
#     print("soory file not found")


# # catching specific exception
# try:
#   m=5
#   f = open('sample1.txt','r')
#   print(f.read())
#   print(m)
#   print(5/2)
#   L = [1,2,3]
#   L[100]
# except FileNotFoundError:
#   print('file not found')
# except NameError:
#   print('variable not defined')
# except ZeroDivisionError:
#   print("can't divide by 0")
# except Exception as e: # here it is generic exceptio which tell about all types of error
#   print(e)


# # else
# try:
#   f = open('sample1.txt','r')
# except FileNotFoundError:
#   print('file nai mili')
# except Exception:
#   print('kuch to lafda hai')
# else:
#   print(f.read()) # in else woa code likhta hai jska liya hum sure hai ki woa error nhi dega
#   # aur ya tbb chlega jbb try shi sa chl rha hai if try shi sa nhi chlega then except wala chlega


# # finally
# # else
# try:
#   f = open('sample1.txt','r')
# except FileNotFoundError:
#   print('file nai mili')
# except Exception:
#   print('kuch to lafda hai')
# else:
#   print(f.read())
# finally:
#   print('ye to print hoga hi')
# # code mai error hoa ya code run hoa jaya finally wala block chlega he.


# # raise Exception
# # In Python programming, exceptions are raised when errors occur at runtime. 
# # We can also manually raise exceptions using the raise keyword.

# # We can optionally pass values to the exception to clarify why that exception was raised

# raise ZeroDivisionError('aise hi try kar raha hu')
# # Java
# # try -> try
# # except -> catch
# # raise -> throw

# class Bank:

#   def __init__(self,balance):
#     self.balance = balance

#   def withdraw(self,amount):
#     if amount < 0:
#       raise Exception('amount cannot be -ve')
#     if self.balance < amount:
#       raise Exception('paise nai hai tere paas')
#     self.balance = self.balance - amount

# obj = Bank(10000)
# try:
#   obj.withdraw(15000)
# except Exception as e:
#   print(e)
# else:
#   print(obj.balance)

# #here raise throw the error means btata hai kya error hai and except phr ush error koa catch krta hai
# # else agar try run krta hai then else bhi run krega

# # Creating custom exceptions

# class MyException(Exception): # eception inherit krna hoga nhi toa raise use nhi kr payenga aur custom class child hoga exception ka
#   def __init__(self,message):
#     print(message)

# class Bank:

#   def __init__(self,balance):
#     self.balance = balance

#   def withdraw(self,amount):
#     if amount < 0:
#       raise MyException('amount cannot be -ve') # yha MyException class ka object bnn rha hai joa constructor koa call krega
#     if self.balance < amount:
#       raise MyException('paise nai hai tere paas')
#     self.balance = self.balance - amount

# obj = Bank(10000)
# try:
#   obj.withdraw(5000)
# except MyException as e:
#   pass
# else:
#   print(obj.balance)

# Why we have to make custom exception class


class SecurityError(Exception):

  def __init__(self,message):
    print(message)

  def logout(self):
    print('logout')

class Google:

  def __init__(self,name,email,password,device):
    self.name = name
    self.email = email
    self.password = password
    self.device = device

  def login(self,email,password,device):
    if device != self.device:
      raise SecurityError('bhai teri to lag gayi')
    if email == self.email and password == self.password:
      print('welcome')
    else:
      print('login error')



obj = Google('nitish','nitish@gmail.com','1234','android')

try:
  obj.login('nitish@gmail.com','1234','windows')
except SecurityError as e:
  e.logout()
else:
  print(obj.name)
finally:
  print('database connection closed')

