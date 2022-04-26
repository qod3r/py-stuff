import numpy as np


image = np.fromfile("bruh.bmp", dtype=np.uint8)
image[1074:] = 0xFF - image[1074:]
image.tofile("bruh_neg.bmp")
