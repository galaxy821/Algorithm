"""
바이러스 [https://www.acmicpc.net/problem/2606]
"""

from collections import deque
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, sys.stdin.readline().strip().split(" "))
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, n+1):
    graph[i].sort()

visit = [0] * (n+1)
count = 0

q = deque()
q.append(1)
visit[1] = True

while q:
    current = q.popleft()

    for i in graph[current]:
        if not visit[i]:
            visit[i] = True
            count += 1
            q.append(i)

print(count)
