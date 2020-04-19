k = int(input("How much? "))
m = 1
for i in range(1, k):
    m = 1 / (1 + m)
print(m+1)
