import numpy as np
import random

def SortPoStoldzu(mass, m, n):
    for j in range(n):
        for i in range(m-1):
            if mass[i][j] > mass[i+1][j]:
                k = mass[i][j]
                mass[i][j] = mass[i+1][j]
                mass[i+1][j] = k
    if m == 1:
        return mass
    else:
        return SortPoStoldzu(mass, m-1, n)

n = 7
m = 7
mass = np.zeros((m,n))
print("Массив:") 
for i in range(m):
    for j in range(n):
        mass[i][j] = random.randint(0, 50)
    print(mass[i])
mass = SortPoStoldzu(mass, m, n)
print("Отсортированный массив:")
for i in range(m):
    print(mass[i])
