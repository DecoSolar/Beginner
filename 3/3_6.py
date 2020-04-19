a = list(input("Введите строку: "))
for i in range(len(a)):
    elem = a[i]
    if elem == '':
        continue
    else:
        k = 0
        for j in range(i, len(a)):
            if a[j] == elem:
                k += 1
                a[j] = ''
        print(elem, "\t", k)
