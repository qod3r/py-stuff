import numpy as np
np.random.seed(0)

def super_sort(row, col):
    A = np.random.randint(1, 101, [row, col])
    B = A.copy()
    print(B)
    B.sort(0, )
    print(B)
    
    # return (A, B)

super_sort(3, 3)