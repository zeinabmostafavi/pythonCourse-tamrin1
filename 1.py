import math

while True:
    print("************************")
    print("1- +")
    print("2- -")
    print("3- *")
    print("4- /")
    print("5- sin")
    print("6- sqrt")
    print("7- fact")
    print("8- tan")
    print("9- cot")
    print("10- pow ^")
    print("11-exit(e)")
    print("____________________________")
    op = input("please Enter operator: ")
    if op == "exit" or op == "e":
        break

    x = int(input("please Enter first number: "))

    if op == "+" or op == "-" or op == "*" or op == "/":
        y = int(input("please Enter second number: "))

    if op == "+":
        result = x + y

    elif op == "-":
        result = x - y

    elif op == "*":
        result = x * y
    elif op == "/":
        result = x / y
    elif op == "power" or op == "^":
        result = x ** y
    elif op == "sin":
        result = math.sin(x)
    elif op == "sqrt":
        result = math.sqrt(x)

    elif op == "fact":
        result = math.factorial(x)

    elif op == "tan":
        result = math.tan(x)

    elif op == "cot":
        result = 1 / (float(math.tan(x)))

    print(result)
