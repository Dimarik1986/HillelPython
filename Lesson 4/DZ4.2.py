mylist = [0, 1, 7, 2, 4, 8]
# mylist = [1, 3, 5]
# mylist = [6]
# mylist = [0]
result = 0
for i in range(len(mylist)):
    if i % 2 == 0:
        result += mylist[i]
result = result * mylist[-1]
print(result)