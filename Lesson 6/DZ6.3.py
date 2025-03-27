digits = 33

while digits > 9:
    x = 1
    for digit in str(digits):
        x *= int(digit)
    digits = x
print(digits)