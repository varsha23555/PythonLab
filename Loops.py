'''loops are used to repeat instruction
while loops
for loops
'''

# while True:
#     print("hello") #this code print the hello infinit time because while is true until it becomes false it keeps printing hello

count = 1 #this variable is called iterator
# while count<= 5: # this conditionis called iteration
#     print("Hello")
#     count += 1
# print(count)

#print the number from 1 to 5
# i = 1
# while i<=5:
#     print(i)
#     i += 1

# #print the number from 5 to 1
# i = 5
# while i>=1:
#     print(i)
#     i-=1

# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

#multiple table of n
# i = 1
# n = int(input("Enter the value of n: "))
# while i <= 10:
#     print(i * n)
#     i += 1

# x = 1
# while x <= 100:
#     print(x)
#     x += 3

# list = [1,4,9,16,25,36,49,64,81,100]
# indx = 1
# while indx < len(list):
#     print(list[indx])
#     indx += 1

# tup = (1,4,9,16,25,36,49,64,81,100)
# n = int(input("Enter the number : "))
# indx = 0
# while indx < len(tup):
#     if(n == tup[indx]):
#         print("value found")
#         break
#     else:
#         print("value not found")
#     indx += 1

# i = 0
# while i <= 5:
#     if(i == 3):
#         i += 1
#         continue
#     print(i)
#     i += 1

'''For loops are used in the sequential traversal. for traversing string, tuple, list etc...
if we are working with iteration, brake, continue in all those cases we use while loop. 
if we are workig with traversing like traversing through elements in tuple, string etc in those cases we use for loop
for loop is used only when we are dealig with tuple, string, list means values should  be present for execute the simple for loop'''

#example
# num = (1,2,3,4,5,6,7)
# for val in num:
#     print(val)

# list = [1,4,9,16,25,36,49,64,81,100]
# for ele in list:
#     print(ele)

# tup = (1,4,9,16,25,36,49,64,81,100) #this search is called leaner search important to know terminology
# num = int(input("Search for number: "))
# for ele in tup:
#     if(num == ele):
#         print("number found", ele)
#         break

''' Range function return and sequence of numbers, startig from zero by default and increments by 1 by default 
and stops before a specified number
'''

# for i in range(5): #range(stop)
#     print(i)

# for i in range(2, 8): #range(start, stop)
#     print(i)

# for i in range(1, 10, 2): #range(start, stop, step size) step size means increase the value by 2 every time
#     print(i)

#print even and odd numbers using range
# for i in range(2, 11, 2):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

#print from 1 to 100 using for and range
# for i in range(1, 101):
#     print(i) 

# for i in range(100, 0, -1):
#     print(i)

# n = int(input("Enter multiple of: "))
# for i in range(1, 11):
#     print(i*n)

'''Pass statment - pass is a place holder that does nothing. it is used as a placeholder for future code
for el in range(10):
    pass #it is a empty loop which skips the loops 
'''

#wrp to find sum of first n numbers
# list = [1, 2, 9]
# indx = 0
# sum = 0
# while indx < len(list):
#     sum = sum + (list[indx])
#     indx += 1

# print(sum)

#WAP to find factorial
n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i +=1

print("factorial", fact)