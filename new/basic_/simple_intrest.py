principle = int(input("enter a value: "))
rate = int(input("enter interest rate: "))
time= int (input("enter the time "))
si=(principle*rate*time)/100
print(f"the interest for {principle} = {si}")
total = (si+principle)
print(f"so total will be {total}  for  {time} years")

