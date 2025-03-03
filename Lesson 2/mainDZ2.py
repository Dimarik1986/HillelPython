number = int(input("Please enter a number: "))
number1 = number % 10

number2 = number % 100//10

number3 = number // 100%10

number4 = number // 1000%10

number5 = number // 10000%10
print(f"{number1}{number2}{number3}{number4}{number5}")