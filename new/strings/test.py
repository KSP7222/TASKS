'''data = {
    1: ["Praneeth", 22, 1999],
    2: ["test", 23, 1998],
    3: ["demo", 24, 1997]
}
for key, value in data.items():
    print(value[0])
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
set1=set(list1)
set2=set(list2)
c= set1.intersection(set2)
common_list = list(c)
print ("common list : ", common_list)'''
list1 = [1, 2, 3, 2, 5, 4]
print(list(set(list1)))\

