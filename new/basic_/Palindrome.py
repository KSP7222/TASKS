a=input("enter a word: ")
x=0
for i in range (len(a) // 2):
    if a[i] != a[-(i + 1)]:
        x=1
        break
if x==1:
    print("not a palindrome")
else:
    print("its a palindrome")