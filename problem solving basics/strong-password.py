"""
HackerRank Challenge - Strong Password

https://www.hackerrank.com/challenges/strong-password/problem

Este script determina o número mínimo de caracteres que devem ser adicionados
a uma senha para que ela seja considerada forte. Uma senha forte é definida como:
- Contendo pelo menos um dígito (0-9)
- Contendo pelo menos uma letra minúscula (a-z)
- Contendo pelo menos uma letra maiúscula (A-Z)
- Contendo pelo menos um caractere especial (!@#$%^&*()-+)
- Tendo no mínimo 6 caracteres
"""

# Python 3

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#


def minimumNumber(n, password):
    """
    Calcula o número mínimo de caracteres que devem ser adicionados à senha
    para torná-la forte.

    Args:
        n (int): Comprimento atual da senha.
        password (str): A senha a ser avaliada.

    Returns:
        int: Número mínimo de caracteres a serem adicionados.
    """
    digits = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    # Inicializa o contador de tipos de caracteres faltantes
    missing = 0

    # Verifica se há pelo menos um dígito na senha
    if not any(c in digits for c in password):
        missing += 1
    
    # Verifica se há pelo menos uma letra minúscula na senha
    if not any(c in lower_case for c in password):
        missing += 1

    # Verifica se há pelo menos uma letra maiúscula na senha
    if not any(c in upper_case for c in password):
        missing += 1

    # Verifica se há pelo menos um caractere especial na senha
    if not any(c in special_characters for c in password):
        missing += 1

    # Retorna o número máximo entre o número de caracteres faltantes e a diferença
    return max(missing, 6 - n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
