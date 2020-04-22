def Rasriadi(n, k):
    p = 0
    m = n
    while m > 9:
        m = n // 10**p
        p +=1
    return n // 10**(p - k)

n = int(input("Введите число: "))
k = int(input("Сколько разрядов показать? "))
print(Rasriadi(n, k))
