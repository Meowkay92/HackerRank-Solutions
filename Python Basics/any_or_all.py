# https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true


# Python 3

# Referencias:
# https://pt.wikipedia.org/wiki/Capicua
# https://hub.asimov.academy/tutorial/funcoes-any-e-all-em-python-um-guia-completo/


N = int(input())  # Lê a quantidade de números da entrada
N_int = map(int, input().split())  # Lê os números da entrada e converte para inteiros
numbers = [x for x in N_int]  # Cria uma lista com os números

# Verifica se todos os números são positivos
positive = all(num > 0 for num in numbers)  

# Verifica se algum número é palíndromo, convertendo num pra string e invertendo com fatiamento de string
palindromic = any(str(num) == str(num)[::-1] for num in numbers)  

# Imprime True se todas as condições forem verdadeiras, False caso contrário
if positive and palindromic:  
    print(True)
else:
    print(False)