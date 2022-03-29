def cached(func):
    cache = {}
    def wrapper(*args, **kwargs):
        nonlocal cache
        if not cache.get(args):
            nc = func(*args, **kwargs)
            cache[args] = nc
            return nc
        else:
            return cache[args]
    return wrapper

@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(10))