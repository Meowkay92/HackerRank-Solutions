# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem


# Python 3


import re

s = re.findall(
    r"[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm][AEIOUaeiou]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])",
    input(),
)  # Encontra todas as ocorrências do padrão na string de entrada

# Explicação: 
# [QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm] -> Corresponde a uma consoante (maiúscula ou minúscula).
# [AEIOUaeiou]{2,} -> Corresponde a duas ou mais vogais (maiúsculas ou minúsculas).
# (?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]) -> Ela garante que a sequência de vogais é seguida por uma consoante, 
# mas não inclui a consoante na correspondência. 


if s:  # Verifica se a lista 's' não está vazia
    for i in s:  # Itera sobre cada elemento (substring) encontrado
        print(i[1:])  # Imprime a substring a partir do segundo caractere (excluindo a primeira consoante)
else:  # Se a lista 's' estiver vazia (nenhuma correspondência encontrada)
    print(-1)  # Imprime -1