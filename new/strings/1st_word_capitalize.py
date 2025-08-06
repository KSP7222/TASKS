text=["hi  myself praneeth"]
a= text[0].split ()
b=" "
for word in a:
    if len(word)>0:
        first=word[0].upper()
        rest=word[1:]
        b+= first + rest +" "
print(b) 