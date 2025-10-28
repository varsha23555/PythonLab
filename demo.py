def re_sum(n):
    if (n != 0):
        return (re_sum(n-1) + n)
    else:
        return 0
    
print(re_sum(3))