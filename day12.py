"""In Python, a dictionary is a built-in data structure that is used to store key-value pairs. It is sometimes also referred to as a "dict." Dictionaries are highly flexible and efficient for mapping keys to values and allow you to perform various operations such as adding, removing, and updating key-value pairs. Here's a basic overview of dictionaries in Python:

"""
# mydict={}
# print(type(mydict))

# Emp1={'name':"Karan",'age':22,'salary':500000}

# print(Emp1)

# Accessing Values:

# You can access values in a dictionary by specifying the associated key in square brackets.

# print(Emp1['age'])


# Adding or Modifying Entries:

# You can add new key-value pairs or modify existing ones.


# Emp1['add']='mumbai'
# print(Emp1)

# Emp1.update({'Empid':101})
# print(Emp1)

# You can remove a key-value pair from a dictionary using the del statement.

# del Emp1['add'] 
# print(Emp1)

# loop through dict

# for  i in Emp1:
#     print(i)
    
# print("---------------------------")
# for  i in Emp1.values():
#     print(i)


# https://www.w3schools.com/python/python_dictionaries_methods.asp #for dict method 


# print(Emp1.items())



#  Nested Dict 

# Empdata={
    
# 'emp1':{'name':'Pragati','age':22,'salary':500000},
# 'emp2':{'name':'shubham','age':23,'salary':700000},
# 'emp3':{'name':'Karan','age':23,'salary':800000},
# 'emp4':{'name':'shubham sawant','age':23,'salary':900000}
  
# }
 
# print(Empdata['emp4']['name'])

# for i in Empdata['emp4'].values():
#     print(i)

# print(Empdata['emp4'].values())

# for i in Empdata:
#     print(Empdata[i])