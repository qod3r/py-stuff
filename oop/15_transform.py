class Transformer:
    def __init__(self):
        self.commands = dict()
    
    def add_command(self, name, func):
        self.commands[name] = func
    
    def transform(self, command, transformable):
        if command in self.commands.keys():
            try:
                return list(map(self.commands[command], transformable))
            # if not iterable
            except TypeError:
                return self.commands[command](transformable)
        else:
            print("no such command")


if __name__ == "__main__":
    t = Transformer()

    t.add_command("make_negative", lambda x: -abs(x))
    t.add_command("square", lambda x: x ** 2)
    t.add_command("strange_command", lambda x: x + 1 if x % 5 == 0 else x)


    l = list(map(int, input().split()))
    
    for i in range(int(input())):
        l = t.transform(input(), l)
    print(*l)