# https://www.hackerrank.com/challenges/validating-the-phone-number/problem


# Python 3

# Referencias:
# https://developers.google.com/edu/python/regular-expressions?hl=pt-br

import re

n = int(input())  # Entrada

for i in range(n):  # Loop que itera 'n' vezes
    strings = input()  # Lê uma string 'strings' da entrada, que representa um número de telefone

    # Verifica se a string corresponde ao padrão de um número de telefone válido
    if(re.match(r'^[7,8,9][0-9]{9}$', strings)):  
        print("YES")  # Se o número for válido, imprime "YES"
    else:
        print("NO")  # Caso contrário, imprime "NO"