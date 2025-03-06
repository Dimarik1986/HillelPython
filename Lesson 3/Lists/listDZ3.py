numbers = [1,2,3,4,5,6,7,8,9]

middle_lists = len(numbers) // 2

if len(numbers) % 2 != 0:
    middle_lists += 1

first_part_lists = numbers[:middle_lists]
second_part_lists = numbers[middle_lists:]

result = [first_part_lists, second_part_lists]
print(result)
