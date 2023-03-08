import numpy as np


def create_kernel(size, sigma):
    center = (size - 1) / 2
    Guass = np.zeros((3, 3))
    for i in range(size):
        x2 = (i - center) ** 2
        for j in range(size):
            y2 = (j - center) ** 2
            Guass[i, j] = np.exp(-(x2 + y2) / (2 * sigma * sigma))
    # 归一化
    Guass /= np.sum(Guass)
    return Guass


kernel = create_kernel(3, sigma=1)
print(kernel)


