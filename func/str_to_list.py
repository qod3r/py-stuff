def from_string_to_list(s, c):
    c += s.split()

a = [1, 2, 3]
from_string_to_list("4 5 6", a)
print(*a)