#  Flow Control 
"""In Python, the if and else statements are used for conditional execution of code. They allow you to specify different blocks of code to be executed depending on whether a certain condition is true or false. Here's the basic syntax for using if and else"""

# age=int(input("Enter your age : "))
# if(age>=18):
#     print("you are adult")

# else:
#     print("you are teenager ")
    
#  if else and elif (Nested If)


# age=int(input("Enter your age : "))
# if(age>=60):
#     print("You are senior citizen ")
# elif(age>=18):
#     print("you are adult")
# else:
#     print("you are teenager ")
    

#  Q1 => take a number from user and check the given number is Odd or Even
#  Q2 => take 3 number from user and check greater among All 


#  ----------------------------Loop In Python -------------------------------

#  For Loop And While Loop

# A for loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item in the sequence. Here's the basic syntax:



# for i in range(1,10):
#     print(i)





# In Python, a while loop is used to repeatedly execute a block of code as long as a specified condition is true. Here's the basic syntax of a while loop:


# num=1
# while num<=10:
#     print(num)
#     num += 1



#  decrement of while loop 

# num=10

# while (num>=1):
#     print(num)
#     num -= 1


# Nested loops in Python refer to placing one loop inside another. This is a common technique used to work with two-dimensional data structures like lists of lists or to perform repetitive tasks that involve multiple levels of iteration. You can nest while loops just like you can nest for loops. Here's an example of a nested while loop

# num=int(input("Enter a number :  "))
# for i in range(num+1):
#     for j in range(i):
#         print("*",end=" ")
#     print("\r")
    

# break statement:

# The break statement is used to exit a loop prematurely, before the loop's normal termination condition is met.
# It's often used with if conditions to exit a loop when a certain condition is satisfied:


# for i in range(1,10):
#     print(i)
#     if(i==5):
#         break
    

# continue statement:

# The continue statement is used to skip the rest of the current iteration of a loop and move on to the next iteration.
# It's commonly used within loops to skip specific iterations based on a condition:

# for i in range(1,10+1):
#     if(i==5):
#         continue
#     print(i)

# for i in range(10):
#     pass
  