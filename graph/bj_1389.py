"""
케빈 베이컨의 6단계 법칙 [https://www.acmicpc.net/problem/1389]
"""

import sys

INF = int(1e9)

n, m = map(int, sys.stdin.readline().strip().split())

dist = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    dist[a][b] = 1
    dist[b][a] = 1

for i in range(1, n):
    dist[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

result = [INF*INF] * (n+1)
for i in range(1, n+1):
    result[i] = sum(dist[i])

min_value = min(result)

for i in range(1, n+1):
    if result[i] == min_value:
        print(i, end="\n")
        break
