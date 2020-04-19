import numpy as np
import random

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
print("Сгенерированный массив вещественных чисел:")
mass = np.zeros((10, 10))
minim0 = b
for i in range(10):
    for j in range(10):
        mass[i][j] = random.uniform(a, b)
        minim = mass[i][j]
        if minim0 > minim:
            minim0 = minim
            num = i + 1
print(mass)
print("Минимальный элемент: ", minim0)
print("Номер строки с минимальным элементом: ", num)
mass2 = mass
k = num - 1
mass3 = np.zeros(10)
for i in range(10):
    mass3[i] = mass2[0][i]
    mass2[0][i] = mass2[k][i]
for i in range(10):
    mass2[k][i] = mass3[i]
print("Массив с перестановленными строками:\n", mass2)
