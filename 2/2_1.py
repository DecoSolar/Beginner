import math

k = int(input("Введите количество X: "))
y = 0
for i in range(1, k + 1):
    print("Введите значения z, b, a, tg для X", i)
    z = float(input("z = "))
    b = float(input("b = "))
    a = float(input("a = "))
    betta = float(input("betta = "))
    x = z**3 - b + a**2 / math.tan(betta)**2
    y += x
    print("X", i, " = ", x)
print("y = ", y)
