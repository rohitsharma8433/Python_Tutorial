# https://github.com/rohitsharma8433

# File handling in Python is a crucial aspect of working with data, as it allows you to read from and write to files. Python provides built-in functions and libraries for working with files, making it relatively easy to perform tasks such as reading text from a file, writing data to a file, and more.

# Here are the fundamental operations for file handling in Python:

# Opening a File:
# You can use the open() function to open a file. It takes two arguments - the file name and the mode in which you want to open the file (read, write, append, etc.). The most common modes are:

# 'r': Read (default)
# 'w': Write (truncate the file if it already exists)
# 'a': Append (create a new file or append to an existing one)
# 'x': it is use to crteate file 




#  creating file through python

# f=open('data.txt','x')

# write into file using write function

# f=open('data.txt','w')
# f.write("ham ja rhe hai ghumne ")
# f.close()



#  Append into file 

# f=open('data.txt','a')
# f.write("hum ke aa gye ")
# f.close()

# read from file 

# f=open('data.txt','r')
# x=f.read()
# print(x)
# f.close()


#  inserting multiline in file
f=open('data.txt','w')
f.write(""" # https://github.com/rohitsharma8433
 
# File handling in Python is a crucial aspect of working with data, as it allows you to read from and write to files. Python provides built-in functions and libraries for working with files, making it relatively easy to perform tasks such as reading text from a file, writing data to a file, and more.

# Here are the fundamental operations for file handling in Python:

# Opening a File:
# You can use the open() function to open a file. It takes two arguments - the file name and the mode in which you want to open the file (read, write, append, etc.). The most common modes are:

# 'r': Read (default)
# 'w': Write (truncate the file if it already exists)
# 'a': Append (create a new file or append to an existing one)
# 'x': it is use to crteate file 
""")

f.close()