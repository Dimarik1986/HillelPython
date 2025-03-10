# mylist = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# mylist = [1, 0, 13, 0, 0, 0, 5]
mylist = [0, 1, 0, 12, 3]
for i in range(len(mylist)):
    if mylist[i] == 0:
        mylist.append(mylist[i])
        mylist.remove(mylist[i])

print(mylist)