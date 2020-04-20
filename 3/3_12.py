import numpy as np

def VvodMatrix(m, n):
    matrix = np.zeros((m, n))
    j = 0
    while j == 0:
        elementi = input("Введите элементы матрицы через пробел: ").split()
        if len(elementi) == m*n:
            j = 1
        else:
            print("Введите", m*n, "символов.")
    k = 0
    for i in range(m):
        for j in range(n):
            matrix[i][j] = elementi[k]
            k += 1
    return matrix


def SlozenieMatrix(m1, m2, m, n):
    m3 = np.zeros((m, n))
    k = 0
    for i in range(m):
        for j in range(n):
            m3[i][j] = m1[i][j] + m2[i][j]
    return m3

def UmnozMatrix(mat1, mat2, m1, n1, m2, n2):
    if n1 != m2:
        return "действие невозможно, т.к. количество столбцов первой матрицы должно быть рано количеству строк второй."
    mat3 = np.zeros((m1, n2))
    for i in range(m1):
        for j in range(n2):
            for l in range(m2):
                mat3[i][j] += mat1[i][l] * mat2[l][j]
    return mat3

j = 0
while j == 0:
    k = int(input("1 - ввод матрицы\n2 - суммирование двух матриц\n3 - умножение двух матриц\n0 - выход\n"))
    if k == 1:
        try:
            m, n = map(int, input("Введите размерность матрицы(через пробел): ").split())
            matrix = VvodMatrix(m, n)
            print("Матрица: \n", matrix)
        except ValueError:
            print("ERROR")
    elif k == 2:
        try:
            m, n = map(int, input("Введите размерность матриц(через пробел): ").split())
            print("Первая матрица: ")
            matrix1 = VvodMatrix(m, n)
            print("Вторая матрица: ")
            matrix2 = VvodMatrix(m, n)
            matrix3 = SlozenieMatrix(matrix1, matrix2, m, n)
            print(matrix1, "\n\t+\n", matrix2, "\n\t=\n", matrix3)
        except ValueError:
            print("ERROR")
    elif k == 3:
        try:
            m1, n1 = map(int, input("Введите размерность первой матрицы(через пробел): ").split()) # ввела 2 3
            print("Первая матрица: ")
            matrix1 = VvodMatrix(m1, n1)    # матрица 1 0 0  1 1 1
            m2, n2 = map(int, input("Введите размерность второй матрицы(через пробел): ").split()) # ввела 3 4
            print("Вторая матрица: ")
            matrix2 = VvodMatrix(m2, n2)    #матрица 1 1 1 0  1 1 0 0  1 0 1 0
            matrix3 = UmnozMatrix(matrix1, matrix2, m1, n1, m2, n2)  # итог 1 1 1 0  3 2 2 0
            print(matrix1, "\n\t*\n", matrix2, "\n\t=\n", matrix3)
        except ValueError:
            print("ERROR")
    elif k == 0:
        j = 1
    else:
        print("ERROR. Try anaig.")
