def ari(op):
    match op:
        case '+':
            return lambda x, y: x + y
        case '-':
            return lambda x, y: x - y
        case '*':
            return lambda x, y: x * y
        case '/':
            return lambda x, y: x / y

print(ari(input())(2,5))