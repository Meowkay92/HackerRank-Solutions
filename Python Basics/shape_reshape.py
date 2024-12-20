# https://www.hackerrank.com/challenges/np-shape-reshape/problem


# Python 3

# Referencias:
# https://numpy.org/doc/stable/reference/routines.array-manipulation.html


import numpy

# Lê a entrada do usuário como uma string de números inteiros separados por espaço,
# mapeia cada número para o tipo `int`, converte em uma lista e cria um array NumPy
a = numpy.array(list(map(int, input().split())))

# Reorganiza o array `a` em uma matriz 3x3 usando a função `numpy.reshape`
# A matriz terá 3 linhas e 3 colunas
print(numpy.reshape(a, (3, 3)))
