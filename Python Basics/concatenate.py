# https://www.hackerrank.com/challenges/np-concatenate/problem


# Python 3

# Importa a biblioteca numpy para manipulação de arrays
import numpy

# Lê os valores de n, m e p. 'n' é o número de linhas da primeira matriz, 
# 'm' é o número de linhas da segunda matriz e 'p' é o número de colunas
n, m, p = map(int, input().split())

# Listas vazias para armazenar as duas matrizes
array_1 = []
array_2 = []

# Lê linhas de inteiros para a primeira matriz
for i in range(n):
    lines = list(map(int, input().split()))  # Converte cada linha de entrada em uma lista de inteiros
    array_1.append(lines)  # Adiciona a linha a primeira matriz

# Lê linhas de inteiros para a segunda matriz
for i in range(m):
    lines = list(map(int, input().split()))  # Converte cada linha de entrada em uma lista de inteiros
    array_2.append(lines)  # Adiciona a linha a segunda matriz

# Converte as listas de matrizes em arrays NumPy
array_1 = numpy.array(array_1)
array_2 = numpy.array(array_2)

# Concatena as duas matrizes ao longo das linhas
print(numpy.concatenate((array_1, array_2), axis=0))
