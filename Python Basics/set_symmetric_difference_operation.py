# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem


# Python 3


# Número de estudantes que leem o jornal em inglês
n = int(input())

# Conjunto de estudantes que leem o jornal em inglês
english = set(map(int, input().split()))

# Número de estudantes que leem o jornal em francês
b = int(input())

# Conjunto de estudantes que leem o jornal em francês
french = set(map(int, input().split()))

# Calcula o tamanho da diferença simétrica entre os conjuntos e exibe o resultado
print(len(english.symmetric_difference(french))) 