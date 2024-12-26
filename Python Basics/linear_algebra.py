# https://www.hackerrank.com/challenges/np-linear-algebra/problem


# Python 3



import numpy as np

# Lê um número inteiro
n = int(input())

# Lê n linhas de entrada, cada uma contendo n elementos separados por espaço,
# e cria uma matriz numpy com esses valores convertidos para float.
A = np.array([input().split() for i in range(n)], dtype=float)

# Calcula o determinante da matriz A usando np.linalg.det, arredonda o resultado
# para duas casas decimais e imprime.
print(round(np.linalg.det(A), 2))
