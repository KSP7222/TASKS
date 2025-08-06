ans=input("enter a sentance: ")
count=0
for char in ans:
    if char == ' ':
        count+=1
count+=1
print("number of words in sentance is: ",count)



