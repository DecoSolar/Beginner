class Worker:

    def __init__(self, fam, st, chaszp, kolvochas):
        self.famil = fam
        self.staz = st
        self.chaszp = chaszp
        self.kolvochas = kolvochas

    def premia(self):
        if self.staz < 1:
            return "Премия рана 0"
        elif self.staz < 3:
            return "Премия рана %s" % ((self.chaszp * self.kolvochas) * 0.05)
        elif self.staz < 5:
            return "Премия рана %s" % ((self.chaszp * self.kolvochas) * 0.08)
        else:
            return "Премия рана %s" % ((self.chaszp * self.kolvochas) * 0.15)

    def zarplata(self):
        return self.chaszp * self.kolvochas

    def dannie(self):
        return "Фамилия: %s\nСтаж: %s\nРазмер часовой заработной платы: %s\nКоличество отработанных часов: %s\nЗарплата: %s\n%s" % (self.famil, self.staz, self.chaszp, self.kolvochas, self.zarplata(), self.premia())


if __name__ == '__main__':
    j = 1
    while j != 0:
        k = int(input("1 - ввести данные\n2 - вывести записанные данные\n3 - выход\n4 - Очистить файл\n"))
        if k == 1:
            fam = input("Введите Фамилию: ")        #Вводим данные
            st = float(input("Введите стаж: "))
            chaszp = int(input("Введите размер часовой заработной платы: "))
            kolvochas = int(input("Введите количество отработанных часов: "))
            work = Worker(fam, st, chaszp, kolvochas)
            f = open('Worker.txt', 'a')             #открываем файл для записи
            dan = work.dannie()
            f.write(dan)                            #записываем введенные данные
            print("Данные записаны в файл Worker.txt")
            f.close
        elif k == 2:
            with open('Worker.txt') as file:
                print(file.read())                  #вывод данных из файла
        elif k == 3:
            j = 0
        elif k == 4:
            file = open('Worker.txt', 'w')
            file.write('')
            file.close
        else:
            print("ERROR. Try again.")
