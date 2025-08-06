count = 0
with open('example.txt') as f:
    for line in f:
        count += len(line.split())
print(count)