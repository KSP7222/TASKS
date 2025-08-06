a= int(input("enter a number: "))
for i in range (1,a):
    j=i*i
    if j == a:  #compare j value with 9
       break
if j == a:
    print(f"sqrt of {a} is {i}")
else:
    print(f"there is no sqrt for {a}")
 