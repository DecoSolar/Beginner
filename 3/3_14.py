import numpy as np

def sort(mas, m, n):
    for i in range(1, m):
        for j in range(n):
            if mas[i-1][j] > mas[i][j]:
                for j in range(n):
                    k = mas[i-1][j]
                    mas[i-1][j] = mas[i][j]
                    mas[i][j] = k
                break
    if m == 1:
        return mas
    else:
        return sort(mas, m-1, n)
        

with open('Dan.txt') as file:
    f = file.readlines()
mass = np.zeros((len(f), 11))
for i in range(len(f)):
    for j in range(11):
        mass[i][j] = f[i][j]
mass = sort(mass, len(f), 11)
print(mass)
file.close()
