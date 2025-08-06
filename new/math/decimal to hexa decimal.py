a = int(input("Enter a number: "))
b = ""
hex = "0123456789ABCDEF"
while a > 0:
    c = a % 16
    b = hex[c] + b
    a = a // 16
print("Hexadecimal is:", b)
