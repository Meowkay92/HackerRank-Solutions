# https://www.hackerrank.com/challenges/py-the-captains-room/problem


# Python 3

k = int(input())  # Lê o número de quartos e converte para inteiro.
rooms = list(map(int, input().split()))  # Lê a lista de números dos quartos, separa-os em uma lista e converte 
                                         # cada elemento para inteiro.

unique_room = set()  # Conjunto vazio com os números dos quartos únicos.
repeat_room = set()  # Conjunto vazio com os números dos quartos repetidos.

for room in rooms:  # Itera sobre cada número de quarto na lista 'rooms'.
    if room in unique_room:  # Se o número do quarto já estiver no conjunto 'unique_room' (ou seja, é repetido).
        repeat_room.add(room)  # Adiciona o número do quarto ao conjunto 'repeat_room'.
    else:  # Caso contrário (ou seja, o número do quarto ainda não foi encontrado).
        unique_room.add(room)  # Adiciona o número do quarto ao conjunto 'unique_room'.

cap_room = unique_room.difference(repeat_room).pop()  
# Encontra a diferença entre os conjuntos 'unique_room' e 'repeat_room' 
# pop() foi usado para remover e retornar o elemento em seguida.
print(cap_room)  # O número do quarto do capitão.