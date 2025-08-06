def sum(a):
    c=0
    while a>0:
        c+=a%10
        a=a//10
    return c
print(sum(234))
