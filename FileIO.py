'''File I/O in python  - python can be used to perform operations on file(read and write data)
types of all files
text files - .txt, ,docx, .log etc #data stored in the form of characters
binary files - .mp4, .mov, .png, .jpeg etc # data is not in the form of characters
we have to open file using f = open("file name", "mode") before performing any operations like read or write.
data = f.read()
f.close() '''

# f = open("Python\demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

'''if we want to read only particular characters'''
# f = open("Python\demo.txt", "r")
# data = f.read(10)
# print(data)
# f.close()

'''to read a line'''
# f = open("Python\demo.txt", "r")
# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()

'''to write in a file.  If we write or append in a file and if that file doesn't exists then python automatically
creates a file and then write'''
# f = open("Python\demo.txt", "w")
# data = f.write("\nIt requires to preapare lot for interview")
# f.close()

# f = open("Python\sample.txt", "w")
# data = f.write("Apply for jobs as soon as possible")
# f.close()

''' r+  --> read + overwrite (pointer starting) no truncate
    w+  --> read + overwrite #truncate all data is vanished before writing
    a+  --> read + append (pointer end) no truncate
'''
 
'''write an code with syntax'''
# with open("Python\demo.txt", "r") as f: 
#     data = f.read()
#     print(data)
'''its not required to write f.close() at the end because with will close it automatically'''

# with open("Python\demo.txt", "w") as f:
#     data = f.write("I want to learn java")

'''delete a file'''
# import os
# os.remove("Python\sample.txt")

# with open("Python\practice.txt", "w") as f:
#     data = f.write("Hi everyone\nwe are learning file I/O\nusing JAVA\nI like programming in java")

'''replace word java to python in the file'''
# with open("Python\practice.txt", "r") as f:
#     data = f.read()
# new_data = data.replace("java", "Python")
# print(new_data)
# with open("Python\practice.txt", "w") as f: #this line of code will replace java to python in original file
#     data = f.write(new_data)

'''search whether word learning exists or not'''
# def check_for_word(word):
#     with open("Python\practice.txt", "r") as f:
#         data = f.read()
#     if(data.find(word) != -1): #if index is -1 then learning don't exist
#         print("found")
#     else:
#         print("not found")

# check_for_word("learning")

'''search for learning exists in which line'''
# def check_for_line(word):
#     data = True
#     line_no = 1
#     with open("Python\practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1

# check_for_line("learning")  

'''overwrite the data in file'''
with open("Python\practice.txt", "r") as f:
    data = f.read()
    
