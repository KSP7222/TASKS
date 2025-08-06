name = input("Enter a name: ")
vowels = "aeiou"
fv = []
for char in name:
    if char in vowels:
        fv.append(char)#char checks characters individually.
        print( char)#printing all the characters

