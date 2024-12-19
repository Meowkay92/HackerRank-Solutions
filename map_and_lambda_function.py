"""
Este módulo implementa funções para gerar números da sequência de Fibonacci
e calcular cubos de números
"""

# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem


# Python 3

# Referencias:
# https://www.w3schools.com/python/python_lambda.asp
# https://pythonacademy.com.br/blog/funcoes-lambda-no-python



cube = lambda x: x**3
"""
Função lambda que calcula o cubo de um número.

Args:
    x (int/float): O número que será elevado ao cubo.

Returns:
    int/float: O resultado de x³.

Exemplo:
    >>> cube(3)
    27
    >>> cube(2)
    8
"""

def fibonacci(n):
    """
    Gera os n primeiros números da sequência de Fibonacci.
    A sequência começa com [0, 1] e cada número seguinte
    é a soma dos dois números anteriores.

    Args:
        n (int): Quantidade de números da sequência a serem gerados.
                Deve ser um número inteiro positivo.

    Returns:
        list: Lista contendo os n primeiros números da sequência de Fibonacci.

    Notas:
        - Se n <= 0, retorna uma lista vazia
        - Se n == 1, retorna [0]
        - Se n == 2, retorna [0, 1]
    """
    # Inicializa a lista com os dois primeiros números da sequência
    l = [0, 1]
    
    # Gera os próximos números até atingir o tamanho desejado
    for i in range(2, n):
        
        # Cada novo número é a soma dos dois anteriores
        l.append(l[i-2] + l[i-1])
    
    # Retorna exatamente n números da sequência
    return(l[0:n])