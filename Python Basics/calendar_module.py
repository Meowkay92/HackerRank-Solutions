# https://www.hackerrank.com/challenges/calendar-module/problem|


# Python 3

"""
Referencias: 
https://docs.python.org/3/library/calendar.html
"""

import calendar

def main():
    """
    Lê uma data no formato 'MM DD YYYY' a partir da entrada do usuário, 
    converte os valores para inteiros e determina o dia da semana correspondente.
    O nome do dia da semana é impresso em letras maiúsculas.

    A função calendar.weekday() é usada para obter o índice do dia da semana
    (0 para segunda-feira, 6 para domingo), e a função calendar.day_name[] 
    é utilizada para obter o nome completo do dia da semana.
    """

    # Lê a data (mês, dia, ano) como uma string, divide e converte para inteiros
    date = list(map(int, input()).split(' '))

    # Calcula o dia da semana e imprime o nome correspondente em maiúsculas
    print(calendar.day_name[calendar.weekday(date[2], date[0], date[1])].upper())

if __name__ == '__main__':
    main()
