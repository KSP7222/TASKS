a=int(input("enter a number: "))
p=0
for i in range (1,a):
    if a%i==0:
        p+=i
if p==a:
    print("perfect number")
else:
    print("not perfect")            
    