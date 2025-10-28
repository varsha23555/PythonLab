''' Dictionaries are used to store data value in the form of key:value pairs.
they are unordered, mutable(changable) and don't allow duplicate keys.
dict = {
"name" : "Varsha"
"age" : "23"
"GPA" : "3.2"
}
'''

# info = {
#     "name" : "Varsha",
#     "age" : "30",
#     "marks" : [90, 74.5, 80],
#     "subjects" : ("python", "C", "Java"),
#     "Gender" : "Female",
#     23 : 45.6
# }
# print(info)
# print(info["name"])
# print(info["Gender"])
# info["name"] = "Anvika"
# print(info)

# null_dict = {}
# print(null_dict)

###Nested dictionary
#dictionary under another dictionary. Under value we can create another dictonary.

student = {
    "name" : "varsha",
    "age" : 23,
    "subjects" : {
        "phy" : 90,
        "Chem" : 98,
        "math" : 67,
        "bio" : 78
    }
}

# print(student)
# print(student["subjects"]["math"])

'''Methods in dictionary'''
#dictionary.keys()

# print(student.keys())
# print(list(student.keys())) #to print the values in the form of list
# print(student.values())
# print(student.items())
# student.update({"City" : "Delhi"})
# print(student)

# #update and new dict work similarly
# new_dict = {"ssn" : "234445556", "GPA" : "3.4"}
# student.update(new_dict)
# print(student)

# print(student.get("name"))


''' Set a collection of unordered iteams. Each emelent in the set must be unique and immutable
syntax of set  ---> set = {1,2,3,4,5}
Empty set syntax ---> null_set = set()
set is mutable --> we can add the values and remove the values from the set
elements in the set are immuatble  --> we cannot change the elemts in the sets means we cannot chnage the value og the element
'''

# collection = {9,0,8,7,5,2}
# print(collection)
# print(type(collection))
# null_set = set()
# print(null_set)
# collection.add(6)
# collection.add((1,3,4))
# collection.add("name")
# print(collection)
# collection.remove(2)
# print(collection)
# # collection.clear()
# # print(collection)

# print(collection.pop())
# print(collection.pop())

# set1 = {1,2,3}
# set2 = {2,3,4}
# print(set1.union(set2)) #combines both set values and return new 
# print(set1.intersection(set2)) #combines common values and retuen new   

# dict = {
#     "table" : ("a peice of furniture","list of facts and figures"),
#     "cat" : "a small animal"
# }
# print(dict)

# classrooms = {"python", "Java", "C++", "Java", "python","Javascript", "python","C++", "C"}
# print(len(classrooms))

# marks = {}
# x = int(input("Enter the marks of chem: "))
# y = int(input("enter the marks of math: "))
# z = int(input("Enter the marks of phys: "))
# marks.update({"Chem": x, "math": y, "phys" : z})
# print(marks)

num = {9, "9.0"}
print(num)

#or

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)