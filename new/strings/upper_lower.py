a= "SaI PrAnEeTh"
uc=0
lc=0
for char in a:
    if char.isupper():
        uc+=1
    elif char.islower():
        lc+=1    
print("uppercase: ",uc)
print("lowercase: ",lc)