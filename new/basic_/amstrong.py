x=int(input("enter number: "))
a=str(x)
sum=0
for char in a:
    c=int(char)
    sum+=c**3
    if sum == x:
        print("Armstrong number")
        break
else:
    print("Not an Armstrong number")
