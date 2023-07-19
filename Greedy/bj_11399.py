"""
ATM [https://www.acmicpc.net/problem/11399]
"""

import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().strip().split()))

data.sort()

result = 0

for i in range(n):
    result += sum(data[:i+1])

print(result)
