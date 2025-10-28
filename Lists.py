'''List is similar to an array in python
List is a built-iN data type which stores set if values
IT can store the emlements of different types(int, float, string,...)
marks = [23,34,44,56,12,88]
studentData = ["karan",12,44.3,"Delhi"]
String is immutable
Lists are mutable means value of list can be changed
List slicing - Similar to string slicing
list_name = [starting_indx : Ending_indx] #ending index is not included
marks = [23,45,55,12,98,45,22] - marks[1:4] = [45,55,12]
marks[:5] = [23,45,55,12,98]
marks[4:] = [98,45,22]
marks[-3:-1]= [98,45]'''

#List methods
# list = [3,4,2,5]
# list.append(9)
# print(list) #This is also called as mutating because we are changeing the list

list = [2,6,4,8,3,2]
list.append(5)
print(list)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# list.reverse()
# print(list)
list.insert(3,0) #intert the given value at given index
print(list)
# list.remove(8) #remove the give value
# print(list)
list.pop(2) #remove the given index value
print(list)