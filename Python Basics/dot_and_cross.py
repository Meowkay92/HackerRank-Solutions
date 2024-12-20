# https://www.hackerrank.com/challenges/np-dot-and-cross/problem


# Python 3


import numpy

# Lê a dimensão das matrizes
n = int(input())

# Lê a primeira matriz
# Lê n linhas de entrada, divide cada linha em elementos separados por espaço
# e converte os elementos para inteiros usando int
a = numpy.array([input().split() for i in range(n)], int)

# Lê a segunda matriz (
b = numpy.array([input().split() for i in range(n)], int)

# Calcula o produto escalar (dot product) das duas matrizes usando numpy.dot()
print(numpy.dot(a, b))