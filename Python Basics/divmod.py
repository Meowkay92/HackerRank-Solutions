#  https://www.hackerrank.com/challenges/python-mod-divmod/problem


# Python 3


# Solicita ao usuário que insira dois números inteiros.
a = int(input())
b = int(input())

# Calcula e exibe o quociente da divisão inteira de 'a' por 'b'.
print(a // b)

# Calcula e exibe o resto da divisão inteira de 'a' por 'b'.
print(a % b)

# Exibe os resultados como uma tupla (quociente, resto).
print(divmod(a, b))
