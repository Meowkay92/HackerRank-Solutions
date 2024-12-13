# https://www.hackerrank.com/challenges/polar-coordinates/problem


# Python 3


import cmath

def main():
    """
    Lê um número complexo da entrada padrão, converte para coordenadas polares
    e imprime o módulo e o ângulo em radianos em linhas separadas.

    A conversão de coordenadas cartesianas (x, y) para coordenadas polares (r, θ)
    é feita usando a função cmath.polar. O módulo 'r' é a distância da origem, 
    e o ângulo 'θ' é o ângulo em radianos entre o ponto e o eixo X.
    """

    # Lê o número complexo da entrada
    z = complex(input())

    # Converte para coordenadas polares (módulo, ângulo)
    x, y = cmath.polar(z)

    # Imprime o módulo (distância da origem) e o ângulo (em radianos)
    print(x)
    print(y)


if __name__ == '__main__':
    main()
