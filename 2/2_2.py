N = int(input("Введите число N: "))
k = int(input("Введите степень k: "))
y = 0
for i in range(N+1):
    y += i**k
print("Сумма: ", y)
