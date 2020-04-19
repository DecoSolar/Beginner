import numpy as np

j = 1
name = list()
age = list()
name = np.array(name)
age = np.array(age)
while j != 0:
    n = int(input("1 - ввести данные\n2 - выйти\n"))
    if n == 1:
        a = input("Имя: ")
        b = input("Возраст: ")
        name = np.append(name, a)
        age = np.append(age, b)
        for i in range(len(name)):
            print(i, "-е элементы структуры  объекта Р: ", name[i], age[i])     
    elif n == 2:
        j = 0
    else:
        print("ERROR")
