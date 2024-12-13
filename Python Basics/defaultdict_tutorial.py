# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem


# Python 3

# References:
# https://docs.python.org/3/library/collections.html#collections.defaultdict
#

from collections import defaultdict

# Leitura dos dois primeiros números: n (número de palavras) e m (número de consultas)
n, m = map(int, input().split())

# Lê as palavras e as armazena na lista 'words'
words = [input() for i in range(n)]

# Um defaultdict que armazena uma lista de índices para cada palavra
d = defaultdict(list)

# preenchendo dicionario 'd'
for i, word in enumerate(words):
    d[word].append(i + 1) # A palavra é usada como chave no dicionário e o índice + 1 é adicionado à lista de índices

# Para cada consulta, verifica se a palavra está no dicionário
for j in range(m):
    query = input().strip()
    print(*d[query] if d[query] else [-1])
