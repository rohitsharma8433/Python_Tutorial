"""Certainly! Python functions are blocks of code that perform a specific task and can be reused throughout your program. Here's the basic syntax of defining and using a Python function"""

# Void function

# def greet():
#     print("good morning mumbai ")

# greet()



# -------------------------with parameter -----------------

# def add(num1,num2):
#     print("the addition of two number is : ",num1+num2)


# add(50,60)

#  parameter value from user on runtime 
# num1=int(input("Enter 1st number : "))
# num2=int(input("Enter 2nd number : "))
# def add(value1,value2):
#     print("the addition of two number is : ",value1+value2)

# add(num1,num2)


#  ---------------------------------------with return value --------------------

# def add():
#     num1=int(input("Enter 1st number : "))
#     num2=int(input("Enter 2nd number : "))
#     return num1+num2


# x=add()
# print(x)


# --------------------------with parameter and with return value ------------------

def gst_cal(product,price):
    percent=5
    gst=price*percent/100
    res=gst+price
    print(" your product name is : " ,product)
    return res 
    

print("Your final price is : ",gst_cal("samosa",60))