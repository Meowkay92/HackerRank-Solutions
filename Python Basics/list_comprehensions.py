# https://www.hackerrank.com/challenges/list-comprehensions/problem


# Python 3

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # List Comprehension para gerar as coordenadas [i, j, k]
    # A estrutura geral é:
    # [expressão for item in iterável if condição]
    # Neste caso, a expressão é [i, j, k], que cria uma lista com os valores de i, j e k
    # Os iteráveis são range(x + 1), range(y + 1) e range(z + 1), que geram sequências de números de 0 até x, y e z
    # A condição é i + j + k != n, que filtra as coordenadas cuja soma dos índices é diferente de n
    # Demais informaçoes sobre valores de entrada e variaveis disponiveis no link no topo

    # Solution
    coords = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(coords)

# Codigo com loop for, 
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    coordinates = []

    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i + j + k != n:
                    coordinates.append([i, j, k])

    print(coordinates)