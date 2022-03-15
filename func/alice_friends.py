def add_friends(name, friends):
    if name in alices_friends:
        alices_friends[name] += friends
    else:
        alices_friends[name] = friends


def are_friends(name1, name2):
    return any(name2 in alices_friends[name1], name1 in alices_friends[name2])


def print_friends(name):
    print(*sorted(alices_friends[name]))


alices_friends = dict()
