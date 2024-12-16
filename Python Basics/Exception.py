# https://www.hackerrank.com/challenges/exceptions

# Python 3


# Itera o número de vezes definido pela entrada do usuário
for i in range(int(input())):
    # Recebe dois valores separados por espaço, que serão armazenados nas variáveis 'a' e 'b'
    a, b = input().split()
    try:
        # Tenta realizar a divisão inteira entre 'a' e 'b', convertendo ambos para inteiros
        result = int(a) // int(b)
        # Se a divisão for bem-sucedida, o resultado é impresso
        print(result)

    # Trata o erro caso ocorra uma divisão por zero
    except ZeroDivisionError as e:
        print(f"Error Code: {e}")

    # Trata o erro de valor
    except ValueError as v:
        # Exibe a mensagem de erro personalizada para o caso de valores inválidos para conversão
        print(f"Error Code: {v}")
