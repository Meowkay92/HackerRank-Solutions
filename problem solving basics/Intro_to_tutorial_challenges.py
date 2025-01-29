# https://www.hackerrank.com/challenges/tutorial-intro/problem


# Python 3

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'introTutorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER V
#  2. INTEGER_ARRAY arr
#

def introTutorial(V, arr):
    # Write your code here
    """
    Função para encontrar a posição de um valor específico (V) dentro de uma lista ordenada (arr).
    
    Parâmetros:
    V (int): O valor que queremos encontrar na lista.
    arr (list): Lista de inteiros ordenados em ordem crescente.

    Retorno:
    int: O índice de V dentro da lista arr.
    """
    return arr.index(V)  # Retorna o índice da primeira ocorrência de V em arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input().strip())

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
