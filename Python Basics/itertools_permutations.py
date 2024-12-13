# https://www.hackerrank.com/challenges/itertools-permutations/problem


# Python 3

from itertools import permutations

def main():
    """
    Resolve o desafio 'itertools.permutations' do HackerRank.

    
    Este código gera todas as permutações possíveis de tamanho k de uma string s fornecida
    pelo usuário. As permutações são ordenadas lexicograficamente e, em seguida, cada permutação
    é impressa uma por uma.
    """
    
    # Lê a string s e o número inteiro k da entrada, separados por espaço
    s, k = input().split()
    k = int(k)  # Converte k diretamente para inteiro

    # Gera e ordena as permutações lexicograficamente, em seguida imprime cada permutação
    for i in sorted(permutations(s, k)):
        # Junta os caracteres da permutação e imprime
        print(''.join(i))

if __name__ == '__main__':
    main()
