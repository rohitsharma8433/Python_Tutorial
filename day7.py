"""Variable scope in Python refers to the visibility and accessibility of variables within different parts of a Python program. Python has two main types of variable scope:"""

# Global variable 
# x=10 # Global variable 
# def show():
#     y=20
#     print(x+y)

# show()


# Local variable 

# Variables defined inside a function have local scope.
# They can only be accessed within that specific function.
# Local variables are created when the function is called and destroyed when the function exits.

# name='Pragati '

# def FullName():
#     L_Name='Thik' # Local  Variable 
#     print(name + L_Name)



# FullName()
# # print(name + L_Name) # L_Name is not valid 


# """It's important to understand the concept of variable scope in Python, as it determines where a variable can be accessed and whether it can be modified within a particular context. If a variable with the same name exists in both the local and global scopes, the local variable takes precedence within the function, but it does not affect the global variable with the same name. To modify a global variable from within a function, you need to use the global keyword."""

# name='Pragati '

# def FullName():
#     global L_Name  # Local  Variable 
#     L_Name='Thik'

# FullName()
# print(name + L_Name) 

# L_Name='sharma'
# print(L_Name)

