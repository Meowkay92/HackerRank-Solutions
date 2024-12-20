# https://www.hackerrank.com/challenges/np-inner-and-outer/problem


# Python 3

import numpy  # Importa a biblioteca NumPy para operações com arrays

# Lê a primeira matriz como uma linha de entrada, 
# divide a linha em elementos separados por espaço e converte os elementos para inteiros
a = numpy.array(input().split(), int)

# Lê a segunda matriz (mesmo processo da primeira matriz)
b = numpy.array(input().split(), int)

# Calcula o produto interno
print(numpy.inner(a, b))

# Calcula o produto externo (outer product) dos dois arrays usando numpy.outer()
# O produto externo cria uma matriz onde cada elemento é o produto de um elemento de 'a' por um elemento de 'b'
print(numpy.outer(a, b))