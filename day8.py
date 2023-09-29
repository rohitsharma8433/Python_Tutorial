"""
In Python, a module is a file that contains Python code, including variables, functions, and classes, which can be reused in other Python scripts or programs. Modules are a way to organize and compartmentalize your code, making it more maintainable and reusable.
Here's how you can create and use modules in Py"""
#  Random module 
#  Math   module 
#  Date and Time module 


# Rndom Module 
import random
import math

# print(random.random())
# print(random.random()*100)

# print(math.floor(random.random()*100))

# print(random.randint(1000,9999))

# print(random.randint(1,6))



#  Math Module 

#  https://docs.python.org/3/library/math.html   check this for more function in math module 
# import math

# print(math.factorial(5))


#  Date Time 

# import datetime
# print(datetime.datetime.now())
# from datetime import date
# print(date.today())


import datetime
# https://docs.python.org/3/library/datetime.html  check this for more function in datetime module 
x = datetime.datetime(2002, 12, 16)

print(x.strftime("%b"))

