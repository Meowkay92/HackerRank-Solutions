"""
HackerRank Challenge - Insertion Sort 2

https://www.hackerrank.com/challenges/insertionsort2/problem

Este script implementa o algoritmo de Insertion Sort para ordenar uma lista de
inteiros. Após cada iteração do algoritmo, o estado atual da lista é impresso,
seguindo o formato exigido pelo problema.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    """
    Ordena a lista 'arr' utilizando o algoritmo Insertion Sort e imprime o estado
    da lista após cada iteração.

    Args:
        n (int): Número de elementos na lista.
        arr (list of int): Lista de inteiros a ser ordenada.
    """
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(" ".join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
