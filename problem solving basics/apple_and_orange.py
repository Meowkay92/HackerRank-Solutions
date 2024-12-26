# 




def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Contadores para armazenar o número de maçãs e laranjas que caem na casa
    apple_count = 0
    orange_count = 0
    
    # Verifica cada maçã
    for apple in apples:
        # Calcula a posição onde a maçã cai: posição da árvore + distância da queda
        position = a + apple
        # Verifica se a posição está dentro dos limites da casa (entre s e t)
        if s <= position <= t:
            # Se estiver, incrementa o contador de maçãs
            apple_count += 1
    
    # Verifica cada laranja
    for orange in oranges:
        # Calcula a posição onde a laranja cai: posição da árvore + distância da queda
        position = b + orange
        # Verifica se a posição está dentro dos limites da casa (entre s e t)
        if s <= position <= t:
            # Se estiver, incrementa o contador de laranjas
            orange_count += 1
    
    # Imprime o número de maçãs e laranjas que caem na casa
    print(apple_count)
    print(orange_count)


if __name__ == "__main__":
    s, t = map(int, input().split())
    a, b = map(int, input().split())
    m, n = map(int, input().split())
    apples = list(map(int, input().split()))
    oranges = list(map(int, input().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)