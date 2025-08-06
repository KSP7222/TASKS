a=int(input("enter a number: "))
b=int(input("enter a number: "))
gcd=1
for i in range (1,min(a,b)):
      if a%i==0 and b%i==0: 
        gcd=i
print("gcd: ", gcd)