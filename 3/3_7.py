def kolvosek(chas, minut, sek):
    chassek = chas * 3600 #часы в сек
    minsek = minut * 60 #минуты в сек
    sek3 = sek + chassek + minsek
    return sek3

j = 1
while j != 0:
    k = int(input("1 - Вычитание из времени указанного количества секунд\n2 - подсчёт числа секунд между двумя моментами времени, лежащими в пределах одних суток\n3 - Выход\n"))
    if k == 1:
        chas = int(input("Введите значение времени:\nЧасы: ")) # 4
        minut = int(input("Минуты: "))# 32
        sek0 = int(input("Секунды: "))# 47
        sek1 = int(input("Введите количество секунд: "))# 145
        sek3 = kolvosek(chas, minut, sek0) - sek1
        print("Оставшееся время: ", sek3 // 3600, ":", (sek3 % 3600) // 60, ":", sek3 % 60) #4 : 30 : 22
    elif k == 2:
        chas0 = int(input("Введите первый момент времени:\nЧасы: "))#12
        minut0 = int(input("Минуты: "))#10
        sek0 = int(input("Секунды: "))#12
        chas1 = int(input("Введите второй момент времени:\nЧасы: "))#18
        minut1 = int(input("Минуты: "))#45
        sek1 = int(input("Секунды: "))#0
        sek2 = kolvosek(chas0, minut0, sek0)
        sek3 = kolvosek(chas1, minut1, sek1)
        print("Количество секунд между введенными моментами времени: ", sek3 - sek2)# 23688
    elif k == 3:
        j = 0
    else:
        print("ERROR. Try again.")
