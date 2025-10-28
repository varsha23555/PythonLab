'''def is function definition
a and b are parameters'''
# def cal_sum(a, b): 
#     sum = a + b
#     print(sum)
#     return sum

# cal_sum(3, 4)
# cal_sum(5, 6)
# cal_sum(10, 8)
# cal_sum(24, 78)

'''average of three numbers'''
# def average(a, b, c):
#     avg = (a+b+c)/3
#     print(avg)
#     return avg

# average(10, 23, 31)

'''built-in functions and userdefined function. print(), len(), range() etc...
default paramenters in function. Assiginig a default value to paramenter while writing a function insted to giving
 a parameter value during function call. with this we can call a function without arguments '''
# def mult(a=1, b=2):
#     print(a*b)
#     return a*b

# mult()

'''WAP to print the length of the list'''
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cities = ["mumbai", "Bangalore", "pune", "chennai", "Delhi", "hydrabad"]
heroes = ["SRK", "Salaman", "Amir", "vicky", "Karthik"]
# def len_list(list):
#     print(list)

#len_list(cities)


# def elem_list(list):
#     indx = 0
#     while indx < len(list):
#         print(list[indx], end= ", ")
#         indx +=1

'''or using for loop'''

# def elem_list(list):
#     for i in list:
#         print(i, end=", ")

# elem_list(cities)

'''WAP to print the factriol of n'''


# def fact_num(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)

# fact_num(3)
# fact_num(6)
# fact_num(5)
# fact_num(9)

# def convert(usd):
#     inr = usd * 86
#     print(usd, "USD =", inr, "INR")

# convert(5)
# convert(10)

#WAP to print odd or even

def find_num(n):
    if (n %2 == 0):
        print("Even")
    else:
        print("odd")

find_num(int(input("Enter number: ")))