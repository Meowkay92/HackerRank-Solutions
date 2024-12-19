# https://www.hackerrank.com/challenges/re-group-groups/problem


# Python 3

# Referencias:
#


import re

# Lê a string de entrada
S = input()

# Procura por caracteres alfanuméricos repetidos consecutivamente
# O padrão considera apenas letras e números
match = re.search(r'([a-zA-Z0-9])\1+', S)

# Se encontrou uma repetição, imprime
# Senão, imprime -1
print(match.group(1) if match else -1)