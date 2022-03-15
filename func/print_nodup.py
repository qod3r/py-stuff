def print_without_duplicates(msg, _last_msg = [""]):
    if msg != _last_msg[0]:
        print(msg)
        
    _last_msg[0] = msg


print_without_duplicates("a")
print_without_duplicates("a")
print_without_duplicates("b")
print_without_duplicates("a")
print_without_duplicates("c")
print_without_duplicates("c")
