# https://www.hackerrank.com/challenges/py-check-strict-superset/problem


# Python 3

# Define o conjunto A
A = set(map(int, input().split()))

# Lê o número de outros conjuntos
n = int(input())

# Assumir inicialmente que A é um superconjunto estrito.
strict_set = True

# Itera n vezes para comparar A com cada um dos outros conjuntos
for i in range(n):
    # Define o conjunto B a partir da entrada do usuário, convertendo para inteiros.
    B = set(map(int, input().split()))
    
    # Verifica se A é um superconjunto estrito de B.
    # A.issuperset(B) verifica se A contém todos os elementos de B.
    # A == B verifica se A e B são iguais.
    # Se alguma dessas condições for falsa, A não é um superconjunto estrito de B.
    if not A.issuperset(B) or A == B:
        strict_set = False  # Define strict_set como False, se A nao for strict set de B

# Imprime o valor
print(strict_set)