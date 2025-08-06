a="hi how are you doing"
b=a.split()
longest =" "
for words in b:
    if len(words) > len (longest):
        longest = words
print ("longest word : ", longest)