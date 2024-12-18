# https://www.hackerrank.com/challenges/collections-counter/problem


# Python 3

from collections import Counter

# Número de sapatos disponíveis
number_shoes = int(input())

# Tamanhos dos sapatos disponíveis no estoque
sizes = list(map(int, input().split()))

# Armazena a quantidade de cada numero de sapato no estoque
stock = Counter(sizes)

# Número de clientes
customers = int(input())

# Inicializa o lucro
profit = 0

# Processa os pedidos de cada cliente
for i in range(customers):
    size, price = map(int, input().split())  # Tamanho e preço do sapato desejado
    if stock[size] > 0:  # Verifica se tem no estoque o tamanho solicitado
        profit += price  # Adiciona o valor da venda ao lucro
        stock[size] -= 1  # Reduz o estoque do tamanho vendido

# Lucro total obtido
print(profit)
