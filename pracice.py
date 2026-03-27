import numpy as np

matrix = np.array([[10, 20, 30], [40, 50, 60]])
print(matrix)

print(matrix.ndim)
print(matrix.shape)
print(matrix.size)

print(matrix[0, 1])
print(matrix[1, 2])

row_sum = np.sum(matrix, axis=1)
print(row_sum)