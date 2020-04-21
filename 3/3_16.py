import numpy as np
import random

m = int(input("Введите число строк: "))
n = int(input("Введите число столбцов: "))
matrix = np.zeros((m,n))
for i in range(m):
    for j in range(n):
        matrix[i][j] = random.randint(-100, 100)
    print(matrix[i])
k = np.zeros(n)
for j in range(n):
    for i in range(m):
        if matrix[i][j] < 0:
            k[j] = 0
            break
        else:
            k[j] += matrix[i][j]
print("\n", k)
    
