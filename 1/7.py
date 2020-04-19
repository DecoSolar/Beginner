fio = input("Введите ФИО: ")
g = input("Введите группу: ")
lr = 'Лабораторная работа №1'
g = 'Выполнил(а): ст. гр. ' + g
if len(lr) >= len(g) and len(lr) >= len(fio):
    k = len(lr) + 4
elif len(g) >= len(fio) and len(g) >= len(lr):
    k = len(g) + 4
elif len(fio) >= len(g) and len(fio) >= len(lr):
    k = len(fio) + 4
print(k * '*')
lenstr = k - len(lr) - 5
print("*", lr, lenstr * ' ', "*")
lenstr = k - len(g) - 5
print("*", g, lenstr * ' ', "*")
lenstr = k - len(fio) - 5
print("*", fio, lenstr * ' ', "*")
print(k * '*')
