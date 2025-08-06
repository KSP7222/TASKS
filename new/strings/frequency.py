text = "hello world"
f = {}
for char in text:
    if char in f:
        f[char] += 1
    else:
        f[char] = 1
print("Character frequencies:",f)
