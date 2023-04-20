import random
import numpy as np

# Pega um número aleatório , inteiro entre 2-20
size = random.randint(2, 20)

# Instanciando Matrizes
matrix_A = np.random.random_integers(1, 10, (size, size))
matrix_B = np.random.random_integers(1, 10, (size, size))
matrix_C = np.zeros((size, size))

""""
Retire as linhas abaixo caso queira visualizar as matrizes
print(matrix_A)
print(matrix_B)
print(matrix_C)
"""


def multiply(A, B, C, N):
    """
    Função de multiplicação de matrizes
    """
    for i in range(N):
        for j in range(N):
            C[i][j] = 0
            for k in range(N):
                C[i][j] += A[i][k]*B[k][j]

    return C


matrix_final = multiply(matrix_A, matrix_B, matrix_C, size)

print(matrix_final)
