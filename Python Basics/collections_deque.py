# https://www.hackerrank.com/challenges/py-collections-deque/problem


# Python 3


from collections import deque

# Lê o número de comandos que serão executados
n = int(input())

# Inicializa um deque vazio
d = deque()

# Itera para processar cada comando fornecido pelo usuário
for i in range(n):
    # Lê um comando e e separa em uma lista
    command = input().split()
    
    # Executar diferentes operações no deque
    match command[0]:
        case 'append':  # Adiciona um elemento ao final do deque
            d.append(command[1])
        case 'appendleft':  # Adiciona um elemento ao início do deque
            d.appendleft(command[1])
        case 'pop':  # Remove o último elemento do deque
            d.pop()
        case 'popleft':  # Remove o primeiro elemento do deque
            d.popleft()

# Converte os elementos do deque em uma string separada por espaços
print(' '.join(d))
