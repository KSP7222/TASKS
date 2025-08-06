a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
if a % b == 0:
    print(f"LCM: {a}")
elif b % a == 0:
    print(f"LCM: {b}")
else:
    print(f"LCM: {a * b}")

    
