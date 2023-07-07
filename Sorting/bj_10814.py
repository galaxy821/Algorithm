"""
나이순 정렬 [https://www.acmicpc.net/problem/10814]
"""

import sys

n = int(sys.stdin.readline())

values = list()

for i in range(n):
    age, name = input().strip().split()
    values.append([i, age, name])

values = sorted(values, key=lambda x: (x[1], x[0]))

for i in range(n):
    sys.stdout.write(f"{values[i][1]} {values[i][2]}\n")
