# Indica a quantidade de nomes de países a serem lidos
n = int(input())

# Cria um conjunto vazio 'countries' para armazenar os nomes dos países
countries = set()

# Loop que executa 'n' vezes para ler 'n' nomes de países
for i in range(n):
    # Lê o nome do país e o adiciona ao conjunto 'countries'
    name = input()
    countries.add(name)

# Imprime a quantidade de países únicos
print(len(countries))
