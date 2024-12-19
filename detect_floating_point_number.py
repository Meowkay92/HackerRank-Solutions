# https://www.hackerrank.com/challenges/introduction-to-regex/problem


# Python 3

# Referencias:
# https://docs.python.org/3/howto/regex.html
# https://www.w3schools.com/python/python_regex.asp

# Número de casos de teste
t = int(input())

for _ in range(t):
    n = input().strip()  # Lê e remove espaços extras
    try:
        # Tenta converter para ponto flutuante
        float(n)
        # Verifica se é um número de ponto flutuante não inteiro
        if '.' in n:
            print(True)
        else:
            print(False)
    except ValueError:
        print(False)