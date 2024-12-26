# https://www.hackerrank.com/challenges/mini-max-sum/problem


# Python 3


def mini_max_sum(arr):
    # Calcula a soma total de todos os números
    total = sum(arr)
    
    # A soma mínima é a soma total menos o maior número
    min_sum = total - max(arr)
    
    # A soma máxima é a soma total menos o menor número
    max_sum = total - min(arr)
    
    # Imprime os resultados
    print(min_sum, max_sum)


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    mini_max_sum(arr)