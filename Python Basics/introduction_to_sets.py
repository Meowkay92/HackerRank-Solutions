# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem


# Python 3



# Solution
def average(array):
    # your code goes here
    solution = set(arr)
    return sum(solution) / len(solution)]


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)