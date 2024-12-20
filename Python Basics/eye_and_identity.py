# https://www.hackerrank.com/challenges/np-eye-and-identity/problem


# Python 3


import numpy

numpy.set_printoptions(legacy='1.13')
# Define que os os resultados sejam exibidos no formato da versão 1.13.
# por solicitação do desafio

n, m = map(int, input().split())
# Entrada de dois números inteiros separados por espaço.
# 'n' é o número de linhas, e 'm' o número de colunas da matriz

print(numpy.eye(n, m))
# Cria e imprime uma matriz 2D com dimensões 'n' x 'm'

