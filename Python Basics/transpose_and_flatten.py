# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem


# Python 3


import numpy

# Lê as dimensões da matriz (n linhas e m colunas)
n, m = map(int, input().split())

# Inicializa uma lista vazia para armazenar as linhas
lines = []

# Loop para ler cada linha da entrada
for i in range(n):
    lines.append(list(map(int, input().split())))

# Converte a lista de listas em um array NumPy
arr = numpy.array(lines)

# Transpõe a matriz )
print(numpy.transpose(arr))

# "Achata" a matriz em um array unidimensional
print(arr.flatten())
