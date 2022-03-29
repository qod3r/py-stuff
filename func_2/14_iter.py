from math import sqrt
from random import random

# (dist, x, y)
dist = lambda t: (sqrt(t[0] ** 2 + t[1] ** 2), t[0], t[1])

p = [tuple(random() * 10 - 5 for j in range(2)) for i in range(10)]
p2 = [(1, 2), (2, 1), (0, sqrt(5)), (10, 10)]

print(*p2)
print(*sorted(p2, key=dist))