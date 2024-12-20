# https://www.hackerrank.com/challenges/np-min-and-max/problem


# Python 3



import numpy

# Lê as dimensões da matriz
n, m = map(int, input().split())

# Cada linha contém m elementos separados
# O array é criado com a função numpy.array()
arr = numpy.array([input().split() for i in range(n)], dtype=int)

# Calcula o valor mínimo de cada linha da matriz
# A operação será realizada ao longo das colunas (axis=1)
min_result = numpy.min(arr, axis=1)

# Calcula o valor máximo entre os resultados mínimos das linhas:
# Encontra o valor máximo entre os valores mínimos calculados de cada linha.
max_result = numpy.max(min_result)

# Imprime o resultado final
print(max_result)
