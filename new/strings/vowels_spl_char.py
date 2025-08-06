text = "sai pranEETH"
vowels = "aeiouAEIOU"
result = ""
for char in text:
    if char in vowels:
        result += "*" 
    else:
        result += char
print("Modified text:", result)
