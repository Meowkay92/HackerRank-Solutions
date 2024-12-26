# https://www.hackerrank.com/challenges/most-commons/problem


# Python 3



from collections import Counter

def company_logo(s):
    # Conta a frequência dos caracteres
    counter = Counter(s)
    
    # Ordena os caracteres pela frequência (decrescente) e em ordem alfabética
    sorted_chars = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    
    # Exibe os 3 caracteres mais comuns
    # sorted_chars[i] é uma tupla, onde o primeiro elemento (index 0) é o caractere e o segundo elemento (index 1) é a contagem.
    # A função 'print' exibe o caractere e sua contagem.
    for i in range(3):
        print(sorted_chars[i][0], sorted_chars[i][1])

if __name__ == "__main__":
    s = input()
    company_logo(s)
