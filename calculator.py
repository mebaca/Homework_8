print("Calculator")
number1 = int(input("Enter your first number             "))
operation = input("Choose the operation +, -, *, /     ")
number2 = int(input("Enter your second number            "))
if operation == "+":
    print(number1 + number2)
if operation == "-":
    print(number1 - number2)
if operation == "*":
    print(number1 * number2)
if operation == "/":
    print(number1 / number2)
else:
    print("ERROR")
