from random import randint

glassrus = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
glasseng = 'AEIOUaeiou'
soglasrus = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
soglaseng = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqsrtvwxyz'
stroka = list(input("Введите строку: "))
for i in range(len(stroka)):
    sim = stroka[i]
    if  glassrus.count(sim) == 1 or glasseng.count(sim) == 1:
        stroka[i] = ord(sim)
    elif soglasrus.count(sim) == 1:
        j = randint(0, len(glassrus))
        stroka[i] = glassrus[j]
    elif soglaseng.count(sim) == 1:
        j = randint(0, len(glasseng))
        stroka[i] = glasseng[j]
print("Результат: ", stroka)
        
