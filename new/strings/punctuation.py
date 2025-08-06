text= ("hello hi ! how?")
pun= ("!#$%&'()*+,-./:;<=>?@[]\\^_`'}{|")
c=" "
for char in text:
    if char not in pun:
        c=c+char
print(c)