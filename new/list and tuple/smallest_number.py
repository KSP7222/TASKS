a=[5,10,15,20,25,22]
c=a[0]
for num in a:
    if num < c:
        c=num
print("smallest number: ",c)