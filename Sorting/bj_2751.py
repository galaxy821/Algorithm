"""
수 정렬하기 [https://www.acmicpc.net/problem/2751]
"""

import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

values = list()
for _ in range(n):
    values.append(int(input().strip()))

values.sort()
for i in range(n):
    print(str(values[i])+"\n")
