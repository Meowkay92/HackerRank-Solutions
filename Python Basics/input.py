# https://www.hackerrank.com/challenges/input/problem


# Python 3


# Referencias:
# https://docs.python.org/3/library/functions.html#eval
# https://www.programiz.com/python-programming/methods/built-in/eval
# https://www.w3schools.com/python/ref_func_eval.asp

# Lê dois inteiros
x, k = map(int, input().split())

# avalia e compara com 'k'
print(eval(input()) == k)

