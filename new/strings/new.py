def sum_natural(a):
    if a==1:
        return 1
    else:
        return a+sum_natural(a-1)
print(sum_natural(10))