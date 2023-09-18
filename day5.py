"""Recursion is a programming technique in which a function calls itself to solve a problem. In Python, you can use recursion to solve problems that can be broken down into smaller, similar subproblems. When using recursion, it's essential to have a base case to prevent infinite recursion and a recursive case that breaks the problem down into smaller steps."""
# function recursion 

# def facto(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n * facto(n-1)


# print("the factorial of number is : ",facto(5))




"""A lambda function in Python is a small, anonymous function defined using the lambda keyword. Lambda functions are also known as "anonymous functions" or "lambda expressions." They are typically used for simple operations and are often used when you need a short function for a short period of time."""

x= lambda x , y: x+y
print(x(60,40))