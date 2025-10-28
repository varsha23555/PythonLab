#Conditional Statments
#if-elif-else(syntax)
''' if(condition):
    statment1
    elif(condition):
    statment2
    else:
    statment3
'''

# light = "pink"
# if(light == "green"):
#     print("go")
# elif(light == "Red"):
#     print("stop")
# elif(light == "yellow"):
#     print("look")
# else:
#     print("light is broken")
    

# grade = int(input("Enter grade of a student: "))
# if(grade>=90):
#     grade="A"
# elif(grade>=80 and grade<90):
#     grade="B"
# elif(grade>=70 and grade<80):
#     grade="C"
# else:
#     grade="D"
# print("Grade of a student is : ", grade)


#Nesting
# age = 15
# if(age>=18):
#     print("Can drive")
#     if(age>=80):
#         print("Cannot drive above the age")
# else:
#     print("Cannot drive under the age")
     
#odd or even
# num = int(input("Enter the number : "))
# if(num%2 == 0):
#     print("number entered is even")
# else:
#     print("Number entered is odd")

#Gretest of three numbers entered by the user
# num1 = int(input("Enter first number "))
# num2 = int(input("Enter second number "))
# num3 = int(input("Enter third number "))
# if(num1>num2 and num1>3):
#     print(num1)
# elif(num2>num1 and num2>num3):
#     print(num2)
# else:
#     print(num3)

#multiple of 7
# num = int(input("Enter number: "))
# if(num%7 == 0):
#     print("Number is multiple of 7")
# else:
#     print("Number is not a multiple of 7")

#Gratest of 4numbers
num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))
num3 = int(input("Enter third number "))
num4 = int(input("Enter 4th number: "))
if(num1>=num2 and num1>=num3 and num1>=num4):
    print(num1)
elif(num2>=num3 and num2>=num4):
    print(num2)                                
elif(num3>=num4):
    print(num3)
else:
    print(num4)