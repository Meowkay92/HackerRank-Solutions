"""
Este módulo contém a solução para o desafio "Grid Challenge" do HackerRank.

https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge

A função gridChallenge recebe uma grade representada por uma lista de strings, onde cada
string representa uma linha da grade. A solução consiste em:
1. Ordenar cada linha individualmente em ordem lexicográfica.
2. Verificar se, após a ordenação das linhas, cada coluna da grade também está em ordem
   lexicográfica (não decrescente).

Se todas as colunas estiverem ordenadas, a função retorna "YES". Caso contrário, retorna "NO".
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    """
    Ordena as linhas da grade e verifica se as colunas estão em ordem lexicográfica.

    Primeiro, cada linha da grade é convertida em uma lista ordenada de caracteres.
    Em seguida, para cada coluna, é verificado se os caracteres estão em ordem não
    decrescente (cada caractere deve ser maior ou igual ao caractere da linha anterior).
c
    Args:
        grid (list of str): Lista de strings, onde cada string representa uma linha da grade.

    Returns:
        str: "YES" se todas as colunas estiverem ordenadas, caso contrário "NO".
    """
    # Write your code here
    for i in range(len(grid)):
        grid[i] = sorted(grid[i])
    
    for col in range(len(grid[0])):
        for row in range(1, len(grid)):
            if grid[row][col] < grid[row - 1][col]:
                return "NO"
    
    return "YES"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
