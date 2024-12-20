# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem


# Python 3


import numpy


numpy.set_printoptions(legacy='1.13')

# Entrada contendo números separados por espaço, converte-os para float e cria um array NumPy
a = numpy.array(list(map(float, input().split())))


print(numpy.floor(a))  # Imprime o maior inteiro menor ou igual a cada elemento do array
print(numpy.ceil(a))   # Imprime o menor inteiro maior ou igual a cada elemento do array
print(numpy.rint(a))   # Imprime o inteiro mais próximo de cada elemento do array