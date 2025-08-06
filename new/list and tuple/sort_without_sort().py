x = [2,8,5,9,3,6,1,67]
n = len(x)
for i in range(n):
    for j in range(i + 1, n):
        if x[i] > x[j]:
            temp = x[i]
            x[i] = x[j]
            x[j] = temp

print("Sorted list:", x)

