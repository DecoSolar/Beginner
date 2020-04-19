a = 0
b = 0
with open('1.txt') as file:
        f = file.readlines()
        p = len(f)
        for i in range(p):
                k = len(f[i])
                for j in range(k):
                        if f[i][j] == '{':
                                a += 1
                        elif f[i][j] == '}':
                                b += 1
if a == b:
        fil = open('out.txt', 'w')
        fil.write('Баланс скобок не нарушен.')
        fil.close
        fil = open('out.txt')
        m = fil.readlines()
        print(m)
        fil.close
else:
        fil = open('out.txt', 'w')
        fil.write('Баланс скобок нарушен.')
        fil.close
        fil = open('out.txt')
        m = fil.readlines()
        print(m)
        fil.close
file.close
