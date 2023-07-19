"""
동전 0 [https://www.acmicpc.net/problem/11047]
"""

import sys

n, k = map(int, sys.stdin.readline().split(" "))
moneys = [int(sys.stdin.readline()) for _ in range(n)]
moneys.reverse()

result = 0
left_value = k

for i in moneys:
    if left_value >= i:
        result += left_value // i
        left_value = left_value % i
        if left_value == 0:
            break

print(result)
