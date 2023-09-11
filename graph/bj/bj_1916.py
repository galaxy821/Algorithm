"""
최소비용 구하기
"""

from heapq import heappush, heappop
import sys

INF = int(1e9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().strip().split())
    graph[start].append((cost, end))


def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, cur = heappop(q)

        if dist > distance[cur]:
            continue

        for n_dist, nxt in graph[cur]:
            cost = dist + n_dist

            if cost < distance[nxt]:
                distance[nxt] = cost
                heappush(q, (cost, nxt))


start, end = map(int, sys.stdin.readline().strip().split())
dijkstra(start)
print(distance[end])
