import math
import re

while True:
    num1 = int(input())
    operand = input()

    if operand == "x":
        print("\t", end="")
        print(num1)
        break
    if operand == "!":
        if num1 >= 0:
            print("\t", end="")
            print(math.factorial(num1))
        else:
            print()
        continue

    num2 = int(input())

    print("\t", end="")
    match operand:
        case "+":
            print(num1 + num2)
        case "-":
            print(num1 - num2)
        case "*":
            print(num1 * num2)
        case "/":
            print(num1 // num2)
        case "%":
            print(num1 % num2)
        case _:
            continue
