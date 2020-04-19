import numpy

k = int(input("Введите размер массива: "))
mass = [0 for i in range(k)]
y = 0
for i in range(k):
    mass[i] = float(input("Введите число: "))
    if mass[i] > 2.5:
        y += mass[i]**2
print("Сумма: ", y)
