number1 = int(input("Please enter first number: "))
number2 = int(input("Please enter second number: "))

operator= input("Please enter mathematical operation: ")

match operator:
    case "+":
        result = number1 + number2
        print(result)
    case "*":
        result = number1 * number2
        print(result)
    case "/":
        result = number1 / number2
        print(result)
    case "-":
        result = number1 - number2
        print(result)