# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem


# Python 3



# Solution
def average(array):
    """
    Calcula a média dos elementos únicos de uma lista.

    A função recebe uma lista de números, remove os duplicados e calcula a média 
    dos números distintos presentes na lista.

    Parameters:
    arr (list): Lista de números inteiros.

    Returns:
    float: A média dos números únicos na lista.
    """
    
    # your code goes here
    solution = set(arr)
    return sum(solution) / len(solution)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)