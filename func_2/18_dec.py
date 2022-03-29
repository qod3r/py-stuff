def check_password(func):
    def wrapper():
        if input() != "123":
            print("Access denied")
            return None
        else:
            return func()
    return wrapper

@check_password
def a():
    print("a() called")
    return 1

a()