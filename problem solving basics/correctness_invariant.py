"""
HackerRank Challenge - Correctness Invariant

https://www.hackerrank.com/challenges/correctness-invariant/problem

Este script implementa o algoritmo Insertion Sort para ordenar uma lista de inteiros.
A implementação corrige a condição do laço while para que o algoritmo funcione corretamente
mesmo quando o elemento 'key' deve ser inserido na posição 0 da lista.
"""
def insertion_sort(l):
    """
    Ordena a lista 'lst' utilizando o algoritmo Insertion Sort.

    Para cada elemento da lista (exceto o primeiro), o algoritmo insere o elemento na
    posição correta, deslocando os elementos maiores para a direita.

    Args:
        lst (list of int): Lista de inteiros a ser ordenada.

    Returns:
        None: A lista é ordenada in-place.
    """
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))