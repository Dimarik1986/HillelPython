# mylist = [1, 2, 3, 4, 5, 6, 7, 9]
# mylist = [1, 1, 2, 1]
mylist = [6, 3, 7]
listResult = []
for i in range(len(mylist)):
    listResult.append(mylist[0])
    listResult.append(mylist[2])
    listResult.append(mylist[i-2])
    break

print(listResult)
