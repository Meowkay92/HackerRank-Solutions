# https://www.hackerrank.com/challenges/itertools-combinations/problem


# Python 3

from itertools import combinations

#'s' é uma string e 'k' é um número inteiro.
s, k = input().split()

# A função `combinations` será usada para gerar combinações de elementos da string 's' de tamanho variável
# O loop externo itera de 1 até o valor de 'k' (incluo 'k' com mais um), representando o tamanho das combinações.
for i in range(1, int(k) + 1):
    # A função `combinations(sorted(s), i)` gera todas as combinações de tamanho 'i' de elementos da string 's'.
    # A string 's' é ordenada primeiro
    for j in combinations(sorted(s), i):
        # 'j' é uma tupla contendo uma combinação. '.join(j)` para juntar os elementos da tupla em uma string
        print(''.join(j))
