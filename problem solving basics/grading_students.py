# https://www.hackerrank.com/challenges/grading/problem


# Python 3


def gradingStudents(grades):
    # Lista para armazenar as notas arredondadas
    rounded_grades = []
    
    # Itera sobre cada nota
    for grade in grades:
        # Verifica se a nota é menor que 38
        if grade < 38:
            rounded_grades.append(grade)  # Não arredonda
        else:
            # Calcula o próximo múltiplo de 5
            next_multiple = (grade // 5 + 1) * 5
            # Verifica se a diferença é menor que 3
            if next_multiple - grade < 3:
                rounded_grades.append(next_multiple)  # Arredonda
            else:
                rounded_grades.append(grade)  # Não arredonda
    
    return rounded_grades

# Exemplo de uso
if __name__ == "__main__":
    # Lê o número de notas
    n = int(input())
    
    # Lê as notas
    grades = [int(input()) for _ in range(n)]
    
    # Arredonda as notas e imprime o resultado
    result = gradingStudents(grades)
    for grade in result:
        print(grade)