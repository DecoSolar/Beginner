def аddRightDigit(d, k):
    return k * 10 + d

k = int(input("k = "))
j = 0
while j == 0:
    d1 = int(input("d1 = "))
    if d1 >= 0 and d1 < 10:
        k = аddRightDigit(d1, k)
        print("k = ", k)
        j = 1
    else:
        print("0 <= d1 <= 9. Try again.")
while j == 1:
    d2 = int(input("d2 = "))
    if d2 >= 0 and d2 < 10:
        print("k = ", аddRightDigit(d2, k))
        j = 0
    else:
        print("0 <= d2 <= 9. Try again.")
