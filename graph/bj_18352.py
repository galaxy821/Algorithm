"""
특정 거리의 도시 찾기
"""
from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(n+1)]
visit = [False for _ in range(n+1)]
result = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)

q = deque()
q.append((x, 0))
visit[x] = True

while q:
    cur, cnt = q.popleft()

    if cnt == k:
        result.append(cur)

    for i in graph[cur]:
        if not visit[i]:
            q.append((i, cnt+1))
            visit[i] = True

if len(result) >= 1:
    result.sort()
    for i in result:
        print(i, end="\n")
else:
    print("-1")
