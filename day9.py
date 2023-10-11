#  list in python 

# list1=['Shubham','karan','pragati',55,6.5]
# print(list1)
# print(list1[1])
# print(type(list1))


# for i in list1:
#     print(i)


# list1[2]='Thik'
# print(list1)

# slicing 
# list1=['Shubham','karan','pragati',55,6.5,99,44]

# print(list1[1:8:3])
# print(list1[0:6:2])


# Append in the list
# list1.append("Rohit")
# print(list1)

# print(list1.index('pragati'))

# list1=['shubham','karan','pragati']
# list1.sort()
# print(list1)


# cars = ['Ford', 'BMW', 'Volvo']

# cars.sort()
# print(cars)



# list1=['Shubham','karan','pragati',55,6.5,99,44]

# # print(list1[0::2])
# print(list1[-2])


# list1=[1,2,3,[5,6,[10,20,60],8,9],6,8,19]

# # print(list1[3][2][2])

# # print(list1.index(2))

# # list1.insert([3][2],"rohit")
# # print(list1)

# list1[3][2].insert(1,'rohit')
# # print(l)
# # list1.insert(l,'rohit')
# print(list1)

size=int(input("Enter  size list : "))


User_Input_list=[]


for i in range (size):
    # print(" Enter elment : ",i+1)
    x = int(input())
    # Append 'x' to the list.
    User_Input_list.append(x)

# Print the list
print("List:", User_Input_list)


print(User_Input_list[0])
