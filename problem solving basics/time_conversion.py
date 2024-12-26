# https://www.hackerrank.com/challenges/time-conversion/problem


# python 3

import os

def timeConversion(s):
    # Extrai a parte da hora (os dois primeiros caracteres) e converte para inteiro
    time = int(s[:2])
    
    # Extrai o período (AM ou PM, os dois últimos caracteres)
    period = s[-2:]

    # Verifica se o período é AM
    if period == "AM":
        # Se for 12:00:00 AM, converte para 00:00:00
        if time == 12:
            time = 0
    # Verifica se o período é PM
    elif period == "PM":
        # Se não for 12:00:00 PM, adiciona 12 à hora
        if time != 12:
            time += 12

    # Retorna o horário no formato de 24 horas
    # Usa f-string para formatar a hora com dois dígitos e mantém minutos e segundos
    return f"{time:02d}:{s[3:5]}:{s[6:8]}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
