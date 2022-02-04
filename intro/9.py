while True:
    print("Введите пароли:")
    str1 = input()
    str2 = input()
    
    if len(str1) < 8:
        print("Короткий!\n")
        continue
    
    if str1.find("123") >= 0:
        print("Простой!\n")
        continue
    
    if str1 != str2:
        print("Различаются.\n")
        continue
    
    print("OK")
    break