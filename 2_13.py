import math

n = int(input("Введите n: "))
y = 0
x = 0
for i in range(1, n+1):
    k = math.radians(i)
    x += math.sin(k)
    y += 1/x
print("Сумма рана ", y)
    
