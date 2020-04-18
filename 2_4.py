import math

v = int(input("V = "))
t = int(input("T = "))
g = 9.8
y = math.asin((g * t) / (2 * v))
print("Ugol v radianah: ", y, " & v  gradusah: ", y * 57.2958)
