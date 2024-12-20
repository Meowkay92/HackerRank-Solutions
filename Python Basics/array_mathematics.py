# https://www.hackerrank.com/challenges/np-array-mathematics/problem


# Python 3

import numpy

# Lê as dimensões das matrizes
n, m = map(int, input().split())

# Cria as matrizes 'a' e 'b' e especifica o tipo de dado como inteiro 
a = numpy.array([input().split() for i in range(n)], dtype=int)
b = numpy.array([input().split() for i in range(n)], dtype=int)

# Realiza as operações elemento a elemento entre as matrizes 'a' e 'b' usando as funções do NumPy
print(numpy.add(a, b))         # Soma
print(numpy.subtract(a, b))      # Subtração
print(numpy.multiply(a, b))     # Multiplicação
print(numpy.floor_divide(a, b))  # Divisão inteira
print(numpy.mod(a, b))         # Módulo (resto da divisão)
print(numpy.power(a, b))       # Potência