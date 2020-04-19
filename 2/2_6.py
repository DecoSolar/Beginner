import math

x = int(input("Введите значение x: "))
y = int(input("Введите значение y: "))
x = math.radians(x)
y = math.radians(y)
z = (1 - math.tan(x))**(1 / math.tan(x))
a = math.tan(x)
b = x - y
k = math.cos(b)
l = (1 - a) / (1 / a) + k
print("Ответ: ", l)
