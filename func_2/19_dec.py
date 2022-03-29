def check_password(pw):
    def wrapper(func):
        if input() != pw:
            print("Access denied")
            return None
        else:
            return func()
    return wrapper

@check_password("bruh")
def a():
    print("a() called")
    return 1