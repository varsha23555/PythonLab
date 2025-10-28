'''Tuple is similar to list only difference is tuple is immutable but list is mutable. Immutable means we cannot add any value to tuple.
syntax of tuple.
tuple = (1,2,3,4)
When we write single value in the tuple we should write comma after that value
ex: tup = (5,) if we don't mention comma after the value it is considered as integer. So it is compulsory to write comma
We can print empty tuple as well. tuple  = ()
Slicing in tuple works similar to list.
 '''

# tup = (2,4,5,6,7,8)
# tup = tup[3:5]
# print(tup)

'''tuple.index(element) #This method returens index first occurance  '''
# tuple  = (2,4,1,4,5,6,7)
# print(tuple.index(7))

'''tuple.cont(element)  #This method count the total occurance of the element'''
#print(tuple.count(4))

#Examples

# a = input("Enter first movie name: ")
# b = input("Enter second movie name: ")
# c = input("Enter third movie name: ")
# list = [a, b, c]
# print(list)

# movie = []
# a = input("Enter first movie name: ")
# b = input("Enter second movie name: ")
# c = input("Enter third movie name: ")
# movie.append(a)
# movie.append(b)
# movie.append(c)
# print(movie)

# list = [3,4,5,4,3]
# print(list)
# print(list.copy())

# orgvalue = [1,2,2,1]
# copyval = orgvalue.copy()
# copyval.reverse()
# if(copyval == orgvalue):
#     print("True")
# else:
#     print("False") 

# grade = ("C","D","A","B","A","A","D")
# print(grade.count("A"))

grade = ["C","D","A","B","A","A","D"]
grade.sort()
print(grade)