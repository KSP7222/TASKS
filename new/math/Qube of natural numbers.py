n = int(input("Enter a number: "))
sum_qubes = 0
for i in range(1, n + 1):
    sum_qubes += i ** 3
print("Sum of qubes:", sum_qubes)
