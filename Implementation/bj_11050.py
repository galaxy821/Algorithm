"""import math

n, k = map(int, input().split())

result = math.factorial(n)/math.factorial(k)*math.factorial(n-k)
print(result)

# 다른 풀이
"""
import math


def factorial_n_k(n, k):
    value = 1
    for i in range(n, (n-k), -1):
        value *= i
    return value


n, k = map(int, input().split())
print(factorial_n_k(n, k)//math.factorial(k))
