# https://www.hackerrank.com/challenges/default-arguments/problem


# Python 3


class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()  # Cria uma nova instância de EvenStream
    for _ in range(n):
        print(stream.get_next())

queries = int(input())
for _ in range(queries):
    stream_name, n = input().split() 
    if stream_name == "even":
        print_from_stream(n) 
    else:
        print_from_stream(n, OddStream())