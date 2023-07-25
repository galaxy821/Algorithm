"""
DFS와 BFS
"""

from collections import deque
import sys


def dfs(graph, v, n):  # 재귀 대신 스택으로 dfs 구현
    q = deque()
    result = []
    visit = [False for _ in range(n+1)]

    q.append(v)

    while q:
        cur = q.popleft()
        if cur not in result:
            result.append(cur)

        for node in sorted(graph[cur], reverse=True):
            if not visit[node]:
                q.appendleft(node)
                visit[cur] = True

    print(*result, end="\n")


def bfs(graph, v, n):
    q = deque()
    result = []
    visit = [False for _ in range(n+1)]

    q.append(v)
    result.append(v)
    visit[v] = True

    while q:
        cur = q.popleft()

        for node in graph[cur]:
            if not visit[node]:
                q.append(node)
                result.append(node)
                visit[node] = True

    print(*result, end='\n')


n, m, v = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(n+1)]
visit = [False for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

for ver in graph:
    ver.sort()

dfs(graph, v, n)
bfs(graph, v, n)
