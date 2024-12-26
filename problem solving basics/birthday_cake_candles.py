# https://www.hackerrank.com/challenges/birthday-cake-candles/problem


# Python 3


def birthday_cake_candles(candles):
    # Encontra a altura da vela mais alta
    max_height = max(candles)
    
    # Conta quantas velas têm a altura máxima
    count = candles.count(max_height)
    
    # Retorna o resultado
    return count


if __name__ == "__main__":
    n = int(input())
    candles = list(map(int, input().split()))
    result = birthday_cake_candles(candles)
    print(result)