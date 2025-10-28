'''Recursion: When a function call itself repeatedly. recursion is similar to loops'''
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)

# show(5)

'''FACTORIAL OF N  ----> n! = (n-1)! * n'''
# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return fact(n-1) * n
    
# print(fact(9))


'''print list'''
def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

al = ["a", "b", "c", "d", "e"]
print_list(al)
    

'''sunm of first n natural numbers'''
# def sum(n):
#     if(n == 0):
#         return 0
#     else:
#         return sum(n-1) + n
    
# clac_sum = sum(5)
# print(clac_sum)
