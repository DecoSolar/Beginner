import numpy as np

j = 1
l = []
mass = np.array(l)
while j != 0:
    a = int(input("Введите число: "))
    if a >= 0:
        mass = np.append(mass, a)
        print(mass)
    else:
        j = 0
