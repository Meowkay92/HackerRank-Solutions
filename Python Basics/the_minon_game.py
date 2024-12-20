# https://www.hackerrank.com/challenges/the-minion-game/problem


# Python 3

def minion_game(string):
    # Variáveis para as pontuações de Stuart e Kevin
    stuart = 0
    kevin = 0
    
    # Armazena o tamanho da string fornecida
    length = len(string)
    
    # Definindo as vogais
    vowels = 'AEIOU'
    
    # Loop que percorre cada caractere da string
    for i in range(length):
        # Se o caractere for uma vogal, a pontuação de Kevin é incrementada
        if string[i] in vowels:
            kevin += (length - i)  
        else:
            # Caso contrário, a pontuação de Stuart é incrementada
            stuart += (length - i)  
    
    # Comparação das pontuações de Stuart e Kevin para determinar o vencedor
    if stuart > kevin:
        # Se Stuart tiver mais pontos, imprime "Stuart" seguido de sua pontuação
        print(f"Stuart {stuart}")
    elif kevin > stuart:
        # Se Kevin tiver mais pontos, imprime "Kevin" seguido de sua pontuação
        print(f"Kevin {kevin}")
    else:
        # Se as pontuações forem iguais, imprime "Draw" (empate)
        print("Draw")
