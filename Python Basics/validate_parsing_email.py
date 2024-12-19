# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem


# Python 3


import re
import email.utils

# Lê o número de casos de teste da entrada padrão.
n = int(input())

# Itera n vezes para cada caso de teste.
for _ in range(n):
    # Lê uma linha de entrada (no formato Nome <email>) e separa o nome do e-mail.
    nome, endereco_email = email.utils.parseaddr(input())

    # Define a expressão regular para validar o endereço de e-mail.
    # A regex foi modificada para corresponder às regras específicas do HackerRank:
    #   1. O nome de usuário deve começar com uma letra.
    #   2. O nome do domínio deve conter apenas letras.
    #   3. O TLD (Top-Level Domain) deve ter entre 1 e 3 letras.
    padrao_email = r"^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$"

    # Verifica se o endereço de e-mail corresponde à expressão regular.
    if re.match(padrao_email, endereco_email):
        # Se o e-mail for válido:
        #   - Usa email.utils.formataddr() para formatar o nome e o e-mail
        #     de volta para o formato "Nome <email>".
        #   - Imprime o resultado formatado na saída padrão.
        print(email.utils.formataddr((nome, endereco_email)))