import numpy as np
np.random.seed(1)

# a
arr_1 = np.full([3, 4], 3)

# b
arr_2 = np.random.randint(0, 10, [2, 4])

# c
print(arr_1.size, arr_2.size)

# d
print(np.concatenate((arr_1, arr_2), axis=0))

# e
e_tup = (1, 8, 6, 5, 8, 3)
arr_3 = np.array(e_tup)

# f
# arr_4 = np.add(np.multiply(3, arr_3), 1)
arr_4 = arr_3 * 3 + 1

# g
arr_5 = np.reshape(arr_3, [2, 3])

# h
print(np.min(arr_5, axis=1))

# i
print(np.average(arr_5))

# j
arr_6 = np.fromfunction(lambda x: x ** 2, [11])

# k
print(arr_6[::2])

# l
print(arr_6[::-1])

# m (the obvious way)
for i in range(0, len(arr_6), 2):
    arr_6[i] = 2

# n
print(49 in arr_6)

# o
A = np.random.randint(-10, 10, [5, 5])
B = A[A < 0]
