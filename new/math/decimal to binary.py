a = int(input("Enter a number: "))
b = " "
while a > 0:
    rem = a % 2
    b=str(rem)+b
    a = a // 2
print("Binary is:", b)
