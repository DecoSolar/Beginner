kolvo = int(input("Введите число треугольников: "))
for i in range(1, kolvo+1):
    a = ' ' * (kolvo - i)
    b = ' +' * i
    c = (a + b + a) * kolvo
    print(c)
