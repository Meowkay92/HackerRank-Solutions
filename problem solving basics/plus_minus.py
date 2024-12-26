# https://www.hackerrank.com/challenges/plus-minus/problem


# Python 3 


def plusMinus(arr):
    # Inicializa contadores para números positivos, negativos e zeros.
    positive = 0
    negative = 0
    zeros = 0
    
    # Itera pelos elementos do array `arr`.
    for i in arr:
        if i > 0:  # Incrementa o contador de positivos se o número for maior que zero.
            positive += 1
        elif i < 0:  # Incrementa o contador de negativos se o número for menor que zero.
            negative += 1
        else:  # Incrementa o contador de zeros se o número for igual a zero.
            zeros += 1
    
    # Calcula e imprime a proporção de números positivos em relação ao tamanho do array.
    print(round(positive / len(arr), 6))
    
    # Calcula e imprime a proporção de números negativos em relação ao tamanho do array.
    print(round(negative / len(arr), 6))
    
    # Calcula e imprime a proporção de zeros em relação ao tamanho do array.
    print(round(zeros / len(arr), 6))