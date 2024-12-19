# https://www.hackerrank.com/challenges/py-set-mutations


# Python 3

# Referencias:
# https://www.w3schools.com/python/python_sets.asp
# https://docs.python.org/3/tutorial/datastructures.html#sets
# https://www.w3schools.com/python/python_ref_set.asp


a = int(input())  # Tamanho do conjunto A 
A = set(map(int, input().split()))  # Lê os elementos do conjunto A e os converte para um conjunto de inteiros
N = int(input())  # Número de operações a serem realizadas

for i in range(N):  # Itera N vezes, uma vez para cada operação
    operation, size = input().split()  # Lê a operação e o tamanho do conjunto
    new_set = set(map(int, input().split()))  # Lê os elementos do novo conjunto e os converte para um conjunto de inteiros

    if operation == "intersection_update":  # Se a operação for intersection_update
        A.intersection_update(new_set)  # Atualiza A com a intersecção de A e new_set
    elif operation == "update":  # Se a operação for update
        A.update(new_set)  # Adiciona os elementos de new_set a A
    elif operation == "symmetric_difference_update":  # Se a operação for symmetric_difference_update
        A.symmetric_difference_update(new_set)  # Atualiza A com a diferença simétrica de A e new_set
    elif operation == "difference_update":  # Se a operação for difference_update
        A.difference_update(new_set)  # Remove os elementos de new_set de A

print(sum(A))  # ISoma do que restou em A

