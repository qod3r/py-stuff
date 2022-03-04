file_count = int(input())
files = dict()

for _ in range(file_count):
    file, *args = input().split(" ")
    
    files.update({file: args})


command_count = int(input())
commands = dict()

for _ in range(command_count):
    command, file = input().split(" ")
    
    commands.update({file: command})

mapping = {
    'read': ['r', 'R'],
    'write': ['w', 'W'],
    'execute': ['x', 'X']
}

print()
for k in commands:
    if any(v in mapping[commands[k]] for v in files[k]):
        print("OK")
    else:
        print("Access Denied")
    # print(commands[k], files[k], mapping[commands[k]])

# print(files, commands)