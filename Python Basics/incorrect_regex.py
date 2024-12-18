# https://www.hackerrank.com/challenges/incorrect-regex/problem


# Pypy 3 (Python 3 indisponivel mo momento da solução)


# Referencias:
# https://pt.wikipedia.org/wiki/Expressão_regular
# https://www.hashtagtreinamentos.com/regex-no-python


# importação para trabalhar com expressões regulares
import re

# Lê o número de casos de teste
T = int(input())

# Loop para processar cada caso de teste
for i in range(T):
    try:
        # Tenta compilar a expressão regular fornecida
        re.compile(input())
        print(True)  # Se for bem-sucedida imprime True
    except:
        print(False)  # Imprime False se a compilação falhar
