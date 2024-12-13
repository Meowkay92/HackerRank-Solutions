# https://www.hackerrank.com/challenges/itertools-product/problem


# Python 3






# Solution 1
import itertools

# Lê a primeira linha de entrada, separa os números e os converte para inteiros
A = list(map(int, input().split()))

# Lê a segunda linha de entrada, separa os números e os converte para inteiros
B = list(map(int, input().split()))  

# Gera o produto cartesiano entre as listas A e B
cartesian = itertools.product(A, B)

# Itera sobre o produto cartesiano e imprime cada par de elementos
for i in cartesian:
    print(i, '', end='')



# Solution 2
import itertools

def main():
    """
    Resolve o desafio 'itertools.product' do HackerRank.
    
    Este código gera o produto cartesiano entre duas listas de inteiros fornecidas 
    pelo usuário. O produto cartesiano consiste em todas as combinações possíveis 
    de pares, onde o primeiro elemento de cada par vem da lista A e o segundo 
    vem da lista B. O resultado é impresso na mesma linha, sem espaços extras entre 
    os pares.
    
    O desafio consiste nas seguintes etapas:
    1. Ler duas listas de inteiros.
    2. Gerar o produto cartesiano dessas listas.
    3. Imprimir o resultado conforme o formato especificado no problema.
    """

    # Lê a primeira linha de entrada, separa os números e os converte para inteiros
    A = list(map(int, input().split()))

    # Lê a segunda linha de entrada, separa os números e os converte para inteiros
    B = list(map(int, input().split()))  

    # Gera o produto cartesiano entre as listas A e B
    cartesian = itertools.product(A, B)

    # Itera sobre o produto cartesiano e imprime cada par de elementos
    for i in cartesian:
        print(i, '', end='')


if __name__ == '__main__':
    main()
