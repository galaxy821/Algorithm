"""
효율적인 해킹 [https://www.acmicpc.net/problem/1325]
"""

from collections import deque
import sys


def bfs(graph, start):
    q = deque()
    q.append(start)
    visit = [False for _ in range(len(graph)+1)]
    visit[start] = True
    count = 0

    while q:
        cur = q.popleft()

        for i in graph[cur]:
            if not visit[i]:
                q.append(i)
                visit[i] = True
                count += 1

    return count


n, m = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

cal_bfs = [0] * (n+1)
for i in range(1, n+1):
    cal_bfs[i] = bfs(graph, i)

max_value = max(cal_bfs)

for i in range(1, n+1):
    if cal_bfs[i] == max_value:
        print(i, end=" ")
