# https://www.hackerrank.com/challenges/decorators-2-name-directory/problem


# Python 3 



# Solução 1 com loop for:

def person_lister(f):
    # Define uma função decoradora que adiciona funcionalidade à função `f`.
    def inner(people):
        # Cria uma lista para armazenar os resultados após formatar as pessoas.
        result = []
        
        # Converte a idade (índice 2) de cada pessoa em `people` de string para inteiro.
        for i in range(len(people)):
            people[i][2] = int(people[i][2])
        
        # Ordena a lista de pessoas por idade usando `operator.itemgetter(2)`.
        # Processa pela ordem de idade
        people.sort(key=operator.itemgetter(2))
        
        # Aplica a função decorada `f` a cada pessoa na lista ordenada.
        for i in people:
            result.append(f(i))
        
        # Retorna a lista de resultados formatados.
        return result
    return inner



# Solução 2 usando lambda:
def person_lister(f):
    def inner(people):
        # Ordena a lista `people` com base na idade (índice 2) convertida para inteiro
        # `lambda x: int(x[2])` define a ordenação como a idade
        people = sorted(people, key=lambda x: int(x[2]))
        
        # Aplica a função `f` a cada pessoa na lista ordenada
        # Retorna uma nova lista com os resultados formatados
        return [f(person) for person in people]
    return inner

