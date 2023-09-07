''' In Python, keywords are reserved words that have specific meanings and cannot be used as identifiers (such as variable names or function names) because they are part of the language's syntax. Here are some common Python keywords: '''

'''
As of my last knowledge update in September 2021, here is a list of all the Python keywords in Python 3.9:

False
None
True
and
as
assert
async
await
break
class
continue
def
del
elif
else
except
finally
for
from
global
if
import
in
is
lambda
nonlocal
not
or
pass
raise
return
try
while
with
yield '''

#  Example 

# if=10
# print(" if")

#  we can't use if as variable 

# --------------------------------------------------------------

'''
In Python, an identifier is a name given to entities such as variables, functions, classes, modules, and other objects. Identifiers are used to uniquely identify these entities in your Python code. Here are some rules and conventions for defining identifiers in Python:'''

# rule of identifier not valid(~,!,@,$,^ including all special character and all number are not valid for variable name only _ is valid (for maintaining space _ is valid ))

#  not valid 

# @=10
# print(@)

# it gives us  error 
#     @=10
#     ^^
# SyntaxError: invalid syntax

# valid 
_=10
# print(_)


# -------------------------------Variable -------------------------------------

# In Python, you can define a variable by assigning a value to a name (the variable identifier). Unlike some other programming languages, Python is dynamically typed, which means you don't need to declare the data type of a variable explicitly. The data type is determined automatically based on the value assigned to the variable. Here's how you can define variables in Python:

# age=10
# name="karan"
# salary=25.5
# is_student=True

# age is a variable that holds an integer value.
# name is a variable that holds a string value.
# salary is a variable that holds a floating-point number.
# is_student is a variable that holds a boolean value (True or False).

# ----------------------------  Datatype -------------------------------------------------

"""Python is a dynamically typed language, which means that you don't need to declare the data type of a variable explicitly. Python determines the data type of a variable based on the value assigned to it. Here are some of the commonly used data types in Python:"""

# Numeric Type"s:

# int: Represents integer values. For example: 5, -10, 1000.
# float: Represents floating-point (decimal) numbers. For example: 3.14, 2.0, -0.5.

# Text Type:
# str: Represents strings of characters. For example: "Hello, world!", 'Python', "123".
# Boolean Type:
# bool: Represents Boolean values, either True or False."


# name="Pragati"
# s_name="Thik"
# age=20
# salary=25.80
# fav_char="P"

# print("Name : ",name)
# print("Surname  : ",s_name)
# print("Age : ",age)
# print("Salary : ",salary,"lac")

# To check datatype use type function

# print(type(name))
# print(type(s_name))
# print(type(age))
# print(type(salary))
# print(type(fav_char))

# ---------------------------- user input in python--------------------------------------

# In Python, you can obtain user input using the input() function. This function allows you to prompt the user for input and then store their response as a string. Here's a basic example:

# Name=input(" Enter your Name : ")
# print(Name)

#  For Int we heve to typecast the varible into int 
# age=input(" Enter your age : ")
# print(age)
# it return str

#  typecast into int,float
# age=int(input(" Enter your age : "))
# print(age)

# age=float(input(" Enter your age : "))
# print(age)

# ------------------------------End for first day-----------------------

# Get the ASCII value of a character
# char = input(" Enter a char : ")
# ascii_value = ord(char)
# print("The ascii value of ",char," char is ",ascii_value)

