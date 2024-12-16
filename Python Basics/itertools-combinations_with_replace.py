# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem


# Python 3


# `combinations_with_replacement` gera combinações com repetição dos elementos do iterável fornecido.
from itertools import combinations_with_replacement

# Lê a entrada do usuário, que consiste em uma string e um número separados por espaço
s = input().split()

# A função `combinations_with_replacement` gera combinações de tamanho igual a int(s[1]) dos elementos de s[0],
# permitindo que os elementos se repitam nas combinações.
for i in combinations_with_replacement(sorted(s[0]), int(s[1])):
    # 'i' é uma tupla com uma combinação. Usamos `''.join(i)` para transformar essa tupla em uma string
    print(''.join(i))

