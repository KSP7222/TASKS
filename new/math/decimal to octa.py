a = int(input("Enter a  number: "))
b = ""
while a > 0:
    c = a % 8
    b = str(c) + b
    a = a // 8
print("Octal is:", b)
