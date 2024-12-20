#   https://www.hackerrank.com/challenges/validating-uid/problem


# Python 3



import re

for i in range(int(input())):  # Lê o número de casos de teste 
    uid = input()  # Lê o UID como uma string
    print(
        "Valid"  # Imprime "Valid" se todas as condições a seguir forem atendidas
        if all(
            [
                len(uid) == 10,  # Verifica se o UID tem exatamente 10 caracteres
                len(re.findall(r"[A-Z]", uid)) >= 2,  # Verifica se o UID tem pelo menos 2 letras maiúsculas
                len(re.findall(r"[0-9]", uid)) >= 3,  # Verifica se o UID tem pelo menos 3 dígitos
                uid.isalnum(),  # Verifica se o UID contém apenas caracteres alfanuméricos
                len(set(uid)) == 10,  # Verifica se não há caracteres repetidos no UID
            ]
        )
        else "Invalid"  # Imprime "Invalid" se qualquer uma das condições acima for falsa
    )
