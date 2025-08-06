a=int(input("enter a number"))
i=1
j=1
c=0
while i<=a or j<=a:
    c=a-j
    print(" " * c,'#' * i )
    i+=2
    j+=1
