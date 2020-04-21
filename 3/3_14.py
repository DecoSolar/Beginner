with open('Dan.txt') as file:
    f = file.readlines()
    f.sort(key = lambda line: int(line.split(' ')[0]))
for i in range(len(f)):
    print(f[i])
file.close()
