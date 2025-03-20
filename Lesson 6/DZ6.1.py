import string

letter_range = input("Please input letter range: ").split("-")

letters = string.ascii_letters
first_index = letters.index(letter_range[0])
last_index = letters.index(letter_range[1])

print(letters[first_index:last_index+1])