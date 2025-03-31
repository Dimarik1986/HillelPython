def common_elements():
    many_set3 = set()
    many_set5 = set()
    for i in range(0, 101):
        if i % 3 ==0:
            many_set3.add(i)
        if i % 5 ==0:
            many_set5.add(i)
    return many_set3.intersection(many_set5)

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")