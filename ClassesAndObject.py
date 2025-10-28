'''Class is a blue print of an object. Class name should always start with capital letter. 
class is a blueprint of object means the that are required for creating a object is defined in a class
and then object is created. like bule print of house is created(class) before building actual house(object)'''

#Creating class
# class Student:
#     name = "Kiran"

#creating object
# s1 = Student()
# print(s1.name)

# class Car:
#     color = "Blue"
#     brand = "BMW"
#     Model = "SUV"

# car1 = Car()
# print(car1.color)
# print(car1.brand)
# print(car1.Model)

'''Constructor - All classes have a function called __init__() function. This init function is 
invoked(execute) during object creation. Which is always executed when the object is being initiated.
If we don't create init function then python will automatically invoke init fucntion for us. in the constructor init()
function the will be always a self parameter which is pointing to intself. Self paramenter is a reference to the
current instance of the class and used to access variables that belongs to the class. init function is called
in every new object creation. variable in the class are called attributes. 

Consrtuctor with only self parameter is called default constructor __init__(self). other than self parameter if
there other paramenters it is called parameterized constructor.

#dEFAULT constructor
def __init__(self):
    pass
    
#parameterized constructor
def __init__(self, name, marks):
    print("new student")
'''

# class Student:
#     college_name = "ABC college" #This is class attribute which is same for all the object(student)
#     def __init__(self, name, marks):
#         self.name = name  #self.name and self.marks are instance attribute which is different for different objects
#         self.marks = marks
#         print(self)
#         print("Adding new student to the database....")

# s1 = Student("karan", 90)
# print(s1.name, s1.marks)

# s2 = Student("Arjun", 98)
# print(s2.name, s2.marks)


'''Attributes - Class attribute with is common for the complete class and its objects
                Instance attribute is different for different objects
Class stores data(attributes) and methods(functions)              
'''
# class Student:
#     college_name = "ABC college"
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
        
#     def welcome(self):
#         print("welcome student", self.name)

#     def getMarks(self):
#         print(self.marks)

# s1 = Student("karan", 98)
# s1.welcome()
# s1.getMarks()

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def avarage(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your average score is: " sum/3)
      
s1 = Student("karan", [90,87,99])
s1.avarage()
