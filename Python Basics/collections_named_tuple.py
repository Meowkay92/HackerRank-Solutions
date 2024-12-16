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
for i in range(n):
    student_data = input().split()
    student = Student(*student_data)
    total_marks += int(student.MARKS)

# Calcula a média das notas
average = total_marks / n

# Exibe a média com duas casas decimais
print(f'{average:.2f}')



# Solução < 4 linha
# funcional, porem nao recomendado devido legibilidade do codigo
from collections import namedtuple

# Lê o número de estudantes 'n' e os campos do 'namedtuple' fornecidos na entrada
n, fields = int(input()), input()


# Cria o namedtuple 'Student' com os campos fornecidos na entrada
# Calcula a média das notas de 'MARKS' para todos os estudantes
# Para cada estudante, a entrada é lida, convertida em 'Student', a nota é extraída e somada.
# A média é calculada dividindo a soma das notas pelo número de estudantes e formatada com 2 casas decimais
Student = namedtuple('Student', fields); print(f'{sum(int(Student(*input().split()).MARKS) for i in range(n)) / n:.2f}')