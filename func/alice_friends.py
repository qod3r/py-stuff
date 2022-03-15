def add_friends(name, friends):
    if name in alices_friends:
        alices_friends[name] += friends
    else:
        alices_friends[name] = friends


def are_friends(name1, name2):
    return name2 in alices_friends[name1]


def print_friends(name):
    print(*sorted(alices_friends[name]))


alices_friends = dict()

add_friends("Алла", ["Марина", "Иван"])
print(are_friends("Алла", "Мария"))
add_friends("Алла", ["Мария"])
print(are_friends("Алла", "Мария"))