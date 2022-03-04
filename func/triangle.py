def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Существует")
    else:
        print("Не существует")
                
triangle(1, 1, 2)
triangle(7, 6, 10)
triangle(20, 13, 17)