"""
지름길 [https://www.acmicpc.net/problem/1446]
"""

import sys
from heapq import heappush, heappop

INF = int(1e9)

n, m = map(int, sys.stdin.readline().strip().split())

graph = [[(i+1, 1)] for i in range(m)]
graph += [[]]

distance = [INF for _ in range(m+1)]
distance[0] = 0

for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if b > m:
        continue
    graph[a].append((b, c))

q = []
heappush(q, (0, 0))

while q:
    cur, dist = heappop(q)

    if dist > distance[cur]:
        continue

    for node, cost in graph[cur]:
        n_cost = cost + dist
        if n_cost < distance[node]:
            heappush(q, (node, n_cost))
            distance[node] = n_cost

print(distance[m])
