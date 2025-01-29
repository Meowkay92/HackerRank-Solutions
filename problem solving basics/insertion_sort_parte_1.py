# https://www.hackerrank.com/challenges/insertionsort1/problem?


# Python 3


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    """
    Realiza a última iteração do Insertion Sort em um array.
    
    Parâmetros:
    n (int): O tamanho do array.
    arr (list): Lista de inteiros que representa o array parcialmente ordenado.

    Retorno:
    Nenhum. A função imprime o array a cada iteração.
    """
    key = arr[-1]  # Último elemento a ser inserido na posição correta
    i = n - 2  # Índice do elemento antes do último

    # Move os elementos para a direita enquanto forem maiores que 'key'
    while i >= 0 and arr[i] > key:
        arr[i + 1] = arr[i]  # Move o elemento para a direita
        print(*arr)  # Imprime o array atualizado
        i -= 1  # Move o índice para trás

    arr[i + 1] = key  # Insere o elemento na posição correta
    print(*arr)  # Imprime o array final


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
