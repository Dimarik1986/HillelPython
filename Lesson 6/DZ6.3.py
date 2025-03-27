digits = 33

while digits > 9:
    product = 1
    for digit in str(digits):
        product *= int(digit)
    digits = product
print(digits)