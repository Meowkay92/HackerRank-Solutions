# https://www.hackerrank.com/challenges/py-set-union/problem


# Python 3



# Lê um número inteiro 'a' que indica a quantidade de elementos no conjunto 'english'
a_eng = int(input())

# Lê 'a' inteiros e os armazena no conjunto 'english'
english = set(map(int, input().split()))

# Lê um número inteiro 'b' que indica a quantidade de elementos no conjunto 'french'
b_fr = int(input())

# Lê 'b' inteiros e os armazena no conjunto 'french'
french = set(map(int, input().split()))

# Cria o conjunto 'n' que é a união entre os conjuntos 'english' e 'french'
n = french.union(english)
print(len(n))
