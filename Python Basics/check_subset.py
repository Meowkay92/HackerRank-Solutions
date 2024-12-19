# https://www.hackerrank.com/challenges/py-check-subset/problem


# Python 3


T = int(input())  # Lê o número de casos de teste

for i in range(T):  # Itera por cada caso de teste
    number_A = int(input())  # Lê o número de elementos no conjunto A
    A = set(map(int, input().split()))  # Lê os elementos do conjunto A e converte para um conjunto de inteiros
    number_B = int(input())  # Lê o número de elementos no conjunto B
    B = set(map(int, input().split()))  # Lê os elementos do conjunto B e converte para um conjunto de inteiros
    print(A.issubset(B))  # Verifica se A é um subconjunto de B e imprime o resultado (True ou False)