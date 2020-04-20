def MinSlovo(stroka, k, slovo, p):
    if k != len(stroka):
        try:                        
            k1 = stroka.index(' ', k, len(stroka))          #длина слова от символа с индексом к до пробела
            kolvo = k1 - k                                  #длина слова
            if kolvo < p:                                   #если длина меньше предыдущего, записываем слово как мин
                slovo.clear()
                for i in range(k, k1):
                    slovo.append(stroka[i])
            fun = MinSlovo(stroka, k1+1, slovo, kolvo)      #рек пока не проверим все слова(если после последнего нет пробела, то ошибка иexcept ValueError) 
        except ValueError:                                  #когда остается последнее слово, после которого нет пробела
            kolvo = len(stroka) - k                         #длина последнего слова
            if kolvo < p:
                slovo.clear()
                for i in range(k, len(stroka)):
                    slovo.append(stroka[i])
            k = len(stroka)
            return slovo
    return slovo


stroka = list(input("Enter string: "))                      #вводим строку
k = 0
p = len(stroka)
slovo = []
minslov = MinSlovo(stroka, k, slovo, p)                     #находим мин слово
print("Min slovo: ", minslov)
