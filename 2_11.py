import math

a = int(input("Введите отрезок.\nНачало: "))
b = int(input("Конец: "))
h = int(input("Укажите шаг: "))
print("Значения у:")
for i in range(a, b+1, h):
    m = math.log1p(i)
    y = 1 / math.tan(m)**2
    print(y)
