# https://www.hackerrank.com/challenges/np-arrays/problem


# Python 3


# Referencias:
# https://numpy.org/doc/stable/reference/routines.array-manipulation.html


import numpy

def arrays(arr):
    """
    Converte uma lista de strings em um array NumPy com elementos do tipo float e inverte a ordem dos elementos.

    Args:
      arr: Uma lista de strings representando números.

    Returns:
      Um array NumPy com os números em ordem inversa e tipo float.
    """
    a = numpy.array(arr, float)  # Converte a lista em um array NumPy de floats
    return numpy.flip(a)  # Inverte o array

arr = input().strip().split(' ')  # Lê a entrada do usuário e divide em uma lista
result = arrays(arr)  # Chama a função para criar e inverter o array
print(result)  # Imprime o array resultante