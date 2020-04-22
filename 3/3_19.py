j= 0
while j == 0:
    k = int(input("1 - Ввести координиты\n2 - Выход\n"))
    if k == 1:
        x1, y1 = map(int, input("Введите x1 y1: ").split())
        x2, y2 = map(int, input("Введите x2 y2: ").split())
        if x1 > 8 or y1 > 8 or x2 > 8 or y2 > 8 or x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0:
            print("ERROR. Try again.")
        else:
            if ((x2 == x1 + 2 or x2 == x1 - 2)and (y2 == y1 + 1 or y2 == y1 - 1)) or ((x2 == x1 + 1 or x2 == x1 - 1) and (y2 == y1 + 2 or y2 == y1 - 2)):
                print("Да.")
            else:
                print("Нет.")
    elif k == 2:
        j = 1
    else:
        print("ERROR. Try again.")
        
