# https://www.hackerrank.com/challenges/itertools-product/problem


# Python 3




# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

A = list(map(int, input().split()))
B = list(map(int, input().split()))  

cartesian = itertools.product(A, B)

for i in cartesian:
    print(i, '', end='')
