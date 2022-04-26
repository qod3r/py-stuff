import numpy as np

def make_field(size):
    return np.zeros([size, size], np.int8)

print(make_field(10))
# print(make_field(30))