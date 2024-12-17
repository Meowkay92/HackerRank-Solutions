# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem


# Python 3


# cod inicial HackerRank
n = int(input())

# cod inicial HackerRank
s = set(map(int, input().split()))

# Número de comandos a serem executados
c = int(input())

# Loop para processar os comandos de manipulação no conjunto
for i in range(c):
    # Lê o comando atual como uma lista de strings
    command = input().split()

    # Verifica qual comando foi dado
    if command[0] == "pop":
        # Remove um elemento arbitrário do conjunto (apenas se não estiver vazio)
        s.pop()
    elif command[0] == "discard":
        # Descarta (remove) o elemento especificado se ele existir no conjunto
        s.discard(int(command[1]))
    elif command[0] == "remove":
        # Remove o elemento especificado do conjunto
        s.remove(int(command[1]))
    else:
        # Exibe caso um comando seja inválido
        print("Comando incorreto")

# Calcula e imprime a soma dos elementos restantes no conjunto
print(sum(s))
