import numpy as np


with open("lines.txt", 'r') as f:
    counter = 0
    a = []
    for line in f:
        counter += 1
        a.append(line)

    print(a[np.random.randint(0, counter)])
    