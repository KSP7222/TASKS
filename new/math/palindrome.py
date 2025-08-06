a = int(input("Enter a number: "))
b = a
c = 0
while a > 0:
    digit = a % 10
    c = c * 10 + digit
    a = a // 10
if b == c:
    print("Palindrome")
else:
    print("Not a palindrome")
