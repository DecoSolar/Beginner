chisla = list(map(int, input("Введите числа: ").split(',')))
summ = 0
for i in range(len(chisla)):
    summ += chisla[i]
print("Сумма введенных чисел равна ", summ)
