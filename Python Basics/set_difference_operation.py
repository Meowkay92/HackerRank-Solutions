# https://www.hackerrank.com/challenges/py-set-difference-operation/problem


# Python 3


# Número de estudantes que leem o jornal em inglês
n = int(input())

# Conjunto de estudantes que leem o jornal em inglês
english = set(map(int, input().split()))

# Número de estudantes que leem o jornal em francês
b = int(input())

# Conjunto de estudantes que leem o jornal em francês
french = set(map(int, input().split()))

# Calcula a diferença entre os dois conjuntos e imprime o tamanho
print(len(english.difference(french)))