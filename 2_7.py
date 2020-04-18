y = 1
p = 5712364
a = 741324
m = 24587
for i in range(1, 16):
    y = (a * y + m) % p
    x = y / p
    #a = a * i * 9
    #m = m * i * 4
    print(x)
