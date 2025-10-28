'''Static method - That don't use self parameter(works at class level). To define static method we use
@staticmethod 
def get_avg():
    print("abc")
'''
'''Abstraction - Hiding the unnecessery details(implementation details) and showing only essential 
details to the user is called abstraction.

Encapsulation - wrapping data and functions into a single unit(object). i.e., capsul is one object were we are 
combining data and functions into single unit.
'''

# class Account:
#     def __init__(self, balance, account_no):
#         self.balance = balance
#         self.account_no = account_no

#     def Debit(self, amount):
#         self.balance -= amount
#         print("Rs", amount, "was debited from your account")

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs", amount, "was credited to your account")

#     def get_balance(self):
#         return self.balance
    
# acc1 = Account(23000, 123456)
# acc1.Debit(1000)
# acc1.credit(2000)
# print(acc1.get_balance())

'''del keyword - Used to delete object properties or the object itself. '''
# class Student:
#     def __init__(self, name):
#         self.name = name
# s1 = Student("varsha")
# print(s1.name)

# del s1.name
# print(s1.name)

'''private attribute and methods - private attribute and methods are meant to be used only within the class
and are not accessible from outside of the class to define private simply put underscore two time before 
method or attribute. can we accessed in the other method with the class'''

# class Student:
#     def __init__(self, __name, marks):
#         self.__name = __name
#         self.marks = marks

# s1 = Student("karan", 90)
# print(s1.marks)
# print(s1.__name) #This is gone a trow error if it is accessed outside of the class

'''Inheritance - when one class derivers the properties(attributes) and method of another class'''
# class Car:
#     @staticmethod
#     def start():
#         print("Car started..")
#     @staticmethod
#     def stop():
#         print("Car stopped..")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("Frotuner")
# print(car1.name)
# print(car1.start())

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcom to class B"

class C(A, B):
    varC = "Welcom to class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

'''Super() method is used to access the methods of parent class'''