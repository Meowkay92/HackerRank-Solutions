# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem


# Python 3


# Referencias:
# https://docs.python.org/2/library/collections.html#collections.namedtuple

from collections import namedtuple

# Lê o número de estudantes
n = int(input())

# Lê os nomes dos campos para o namedtuple 
fields = input().split()

# Cria o namedtuple 'Student' com os campos fornecidos
Student = namedtuple('Student', fields)

# Variável para acumular as notas totais
total_marks = 0

# Laço que lê os dados de cada estudante
for _ in range(n):
    student_data = input().split()
    student = Student(*student_data)
    total_marks += int(student.MARKS)

# Calcula a média das notas
average = total_marks / n

# Exibe a média com duas casas decimais
print(f'{average:.2f}')
