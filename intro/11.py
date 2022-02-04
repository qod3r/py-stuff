height = int(input())

max_len = 2 * height - 1
curr_len = max_len

for i in range(height):
    spaces = curr_len // 2
    asterisks = max_len - spaces * 2
    curr_len -= 2
    print(" " * spaces + "*" * asterisks)
