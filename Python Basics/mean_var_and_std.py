# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem


# Python 3

import numpy

# Dimensões da matriz (n linhas, m colunas)
n, m = map(int, input().split())

# Cria um array NumPy a partir da entrada do usuário
# Lê n linhas de entrada, divide cada linha em elementos separados por espaço
# e converte os elementos para inteiros
array = numpy.array([input().split() for i in range(n)], dtype=int)

# Calcula a média dos elementos de cada linha do array
# axis=1 -> linhas
print(numpy.mean(array, axis=1))

# Calcula a variância dos elementos de cada coluna do array
# axis=0 -> colunas
print(numpy.var(array, axis=0))

# Calcula o desvio padrão de todos os elementos do array
# Arredonda o resultado para 11 casas decimais usando round()
print(round(numpy.std(array), 11))