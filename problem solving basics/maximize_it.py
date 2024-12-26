# https://www.hackerrank.com/challenges/maximize-it/problem


# Python 3


from itertools import product  # Importa a função product para gerar o produto cartesiano

# Lê os valores de K (número de listas) e M (módulo)
K, M = map(int, input().split())

# Lê as K listas de números
# Para cada lista, ignora o primeiro valor (tamanho da lista) e armazena os números restantes
lists = [list(map(int, input().split()))[1:] for i in range(K)]

# Inicializa a variável `result` para armazenar o valor máximo encontrado
result = 0

# Itera sobre todas as combinações possíveis geradas pelo produto cartesiano das listas
for i in product(*lists):
    # Calcula a soma dos quadrados dos números na combinação atual
    # Aplica o módulo M à soma e compara com o valor atual de `result`
    # Atualiza `result` com o maior valor entre o calculado e o valor atual de `result`
    result = max(sum(x * x for x in i) % M, result)

# Imprime o valor máximo encontrado
print(result)