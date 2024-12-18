# https://www.hackerrank.com/challenges/python-power-mod-power/problem


# Python 3


# Rerefencias:
# https://pt.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/fast-modular-exponentiation


# Entradas do usuario
a = int(input())
b = int(input())
m = int(input())

# Mostra a potencia
print(pow(a, b))

# Mostra o calculo modular 
print(pow(a, b, m))