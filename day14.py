"""Error handling in Python is a critical part of writing robust and reliable code. Errors, also known as exceptions, can occur for various reasons, such as invalid inputs, file not found, network issues, and so on. Python provides a way to handle these exceptions to prevent your program from crashing and to provide a better user experience. Here's an overview of error handling in Python :"""

# try,except,finally


# num1=int(input("Enter first number :  "))
# num2=int(input("Enter second  number :  "))

# print(num1+num2)
# print("hello pragati  ")


# try:
#     num1=int(input("Enter first number :  "))
#     num2=int(input("Enter second  number :  "))
#     print(num1+num2)
# except Exception as e:
#     print(e)
    
    

   
# print("hello pragati  ")


# try:
#     num1=int(input("Enter first number :  "))
#     num2=int(input("Enter second  number :  "))
#     print(num1+num2)
# except:
#     print("please enter number only")
    
    

   
# print("hello pragati  ")


# Use  of finally keyword 


def ErrorHandling():
    try:
        lst=['Pragati','Shubham','Karan','Rohit']
        i=int(input("Enter index : "))
        print(lst[i])
        return 1
    except Exception as e:
        print(e)
        return 0
    finally:
        print("hello pragati")


ErrorHandling()