# https://www.hackerrank.com/challenges/symmetric-difference/problem

# Python3

# Lê o número de elementos do primeiro conjunto 'a'
m = int(input())

# Lê o elementod de 'a' e armazena em um conjunto
a = set(map(int, input().split()))

# Lê o número de elementos do segundo conjunto 'b'
n = int(input())

# Lê os elementos do conjunto 'b' e os armazena em um conjunto
b = set(map(int, input().split()))

# Calcula a diferença entre 'a' e 'b'
dif1 = a.difference(b)

# Calcula a diferença entre 'b' e 'a' 
dif2 = b.difference(a)

# União das duas diferenças (diferença simétrica): elementos exclusivos de 'a' ou 'b'
c = dif1.union(dif2)

# Converte o conjunto resultante 'c' para uma lista
result = list(c)

# Ordena a lista em ordem crescente
result.sort()

# Imprime cada elemento da lista 'result' em ordem crescente
for i in range(len(result)):
    print(result[i])
