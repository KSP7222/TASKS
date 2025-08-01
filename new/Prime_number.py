a= int(input("enter a number: "))
x=0
for i in range (2,a):
    if a%i==0:
        x=1
        break
if x==1:
    print(" not prime")
else:
    print ("prime")    