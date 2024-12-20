# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem


# Python

import numpy

# Lê a entrada do usuário
# A função 'map' converte cada valor para inteiro, e 'tuple' cria uma tupla a partir dos números inseridos.
n = tuple(map(int, input().split()))

# Cria um array de zeros com as dimensões especificadas pela tupla 'n'.
# O tipo de dado do array será numpy.int64(pois numpy.int nao é mais funcional)
print(numpy.zeros(n, dtype=numpy.int64))

# Cria um array de uns com as mesmas dimensões de 'n'.'
# O tipo de dado do array também será numpy.int64.
print(numpy.ones(n, dtype=numpy.int64))
