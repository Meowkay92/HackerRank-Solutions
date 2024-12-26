# https://www.hackerrank.com/challenges/re-start-re-end/problem


# Python 3


import re

# Lê a string de entrada onde será procurado o padrão.
s = input()

# Lê o padrão (substring) que será buscado na string.
k = input()

# Compila o padrão k para criar um objeto de padrão (Pattern object) para pesquisa.
pat = re.compile(k)

# Realiza a primeira busca pelo padrão na string s.
m = pat.search(s)

# Se nenhuma correspondência for encontrada, imprime (-1, -1).
if not m:
    print("(-1, -1)")
else:
    # Caso encontre correspondências, entra em um loop para localizar todas.
    while m:
        # Imprime os índices iniciais e finais (exclusive) da correspondência encontrada.
        print("({0}, {1})".format(m.start(), m.end() - 1))
        # Realiza uma nova busca a partir do próximo caractere após o início da última correspondência.
        m = pat.search(s, m.start() + 1)
