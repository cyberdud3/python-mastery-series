import math


def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x


def isFibonacci(n):
    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)


t = int(input())


for t_itr in range(t):
    n = int(input())
    result = isFibonacci(n)
    print('IsFibo' if result == True else 'IsNotFibo')