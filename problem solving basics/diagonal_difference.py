# https://www.hackerrank.com/challenges/diagonal-difference/problem


# Python 3


import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)  # Obtém o tamanho da matriz quadrada (n x n).
    diagonal = [0, 0]  # Armazena as somas das diagonais principal e secundária numa lista

# Percorre cada linha da matriz para calcular as somas das diagonais.
    for i in range(n):
        diagonal[0] += arr[i][i]         # Adiciona o elemento da diagonal principal 
        diagonal[1] += arr[i][n - i - 1] # Adiciona o elemento da diagonal secundária 

# Calcula a diferença absoluta entre as somas das diagonais e retorna o resultado.
    return abs(diagonal[0] - diagonal[1])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')
