# https://www.hackerrank.com/challenges/zipped/problem


# Python 3

# Referencias:
# https://docs.python.org/3.3/library/functions.html#zip
# 


# Lê o número de alunos (n) e o número de disciplinas (x) da entrada.
n, x = map(int, input().split())

# Inicializa uma lista vazia para armazenar as notas dos alunos.
marks = []

# Itera x vezes, uma para cada disciplina.
for i in range(x):
    # Lê as notas dos alunos para a disciplina atual, converte para float e adicionanda à lista marks.
    marks.append(map(float, input().split()))

# Itera sobre as notas dos alunos, agrupadas por aluno usando zip(*marks).
# zip(*marks) transpõe a lista marks, agrupando as notas do primeiro aluno, do segundo aluno, e assim por diante.
for student_marks in zip(*marks):
    # Calcula a média das notas do aluno atual e imprime o resultado.
    print(sum(student_marks) / len(student_marks))
