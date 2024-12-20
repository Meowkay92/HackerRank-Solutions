# https://www.hackerrank.com/challenges/np-sum-and-prod/problem


# Python 3

import numpy  

# Lê os valores de `n` (número de linhas) e `m` (número de colunas) da matriz.
n, m = map(int, input().split())

# Lê as próximas `n` linhas da entrada, onde cada linha contém `m` elementos.
a = numpy.array([input().split() for i in range(n)], dtype=int)

# Calcula a soma de cada coluna da matriz.
sums = numpy.sum(a, axis=0)

# Calcula o produto de todos os elementos no array de somas das colunas.
print(numpy.prod(sums))
