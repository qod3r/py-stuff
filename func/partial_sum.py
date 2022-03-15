def partial(*args):
    res = [0]
    for i, v in enumerate(args):
        res.append(v + res[i])
    
    return res

print(partial(1, 0.5, 0.25, 0.125))
