import numpy as np

A = np.array([[1,1,1],[2,2,2],[3,3,3]])
B = np.array([[1,1,1],[2,2,2],[3,3,3]])
C = np.array([[1,1,1],[2,2,2],[3,3,3]])

result = A @ B @ C
print("Multiplication of the matrices:\n", result)
