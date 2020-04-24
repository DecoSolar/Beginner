import numpy as np
import random

def SelectionSort(mass):
    k = mass[0]
    for i in range(len(mass)-1):
        k = mass[i]
        a = i
        for j in range(i, len(mass)):
            if mass[j] < k:
                k = mass[j]
                a = j
        mass[a] = mass[i]
        mass[i] = k
    return mass

def ShakeSort(mass, n, m):
    if n == m or n == m+1:
        return mass
    else:
        k = mass[n]
        a = n
        b = m
        l = mass[m]
        for i in range(n, m+1):
            if k > mass[i]:
                k = mass[i]
                a = i
            elif l < mass[i]:
                l = mass[i]
                b = i
        if b == n or a == m:
            b = a
            k = mass[a]
            mass[a] = mass[n]
            mass[n] = k
            l = mass[b]
            mass[b] = mass[m]
            mass[m] = l
        else:
            k = mass[a]
            mass[a] = mass[n]
            mass[n] = k
            l = mass[b]
            mass[b] = mass[m]
            mass[m] = l
        return ShakeSort(mass, n+1, m-1)

def RandomMass(n):
    mass = np.zeros(n)    
    for i in range(n):
        mass[i] = random.randint(0, 50)
    print(mass)
    return mass


j = 0
while j != 1:
    k = int(input("1 - Сортировка выбором\n2 - Шейкер сортировка\n3 - Выход\n"))
    if k == 1:
        n = int(input("Введите размерность массива: "))
        mass = RandomMass(n)
        print("Отсортированный массив:\n", SelectionSort(mass))
    elif k == 2:
        n = int(input("Введите размерность массива: "))
        mass = RandomMass(n)
        print("Отсортированный массив:\n", ShakeSort(mass, 0, n-1))
    elif k == 3:
        j = 1
        
    else:
        print("ERROR")

        
