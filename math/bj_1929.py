"""
소수 구하기 [https://www.acmicpc.net/problem/1929]
"""
import math


def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


n, m = map(int, input().split())

if n == 1:
    n = 2

for i in range(n, m+1):
    if is_prime(i):
        print(i, end="\n")

# dynamic programming
# n, m = map(int, input().split())
# values = [True] *(m+1)
# values[0] = False
# values[1] = False

# for i in range(2, m+1) :
#     if values[i] :
#         for j in range(2*i, m+1, i) :
#             values[j] = False

# for i in range(n, m+1) :
#     if values[i] :
#         print(i, end="\n")
