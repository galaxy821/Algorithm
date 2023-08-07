"""
경로 찾기
"""

# floyd warshall 풀이
import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip().split()))
         for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k]+graph[k][j] > 1:
                graph[i][j] = 1

for i in range(n):
    print(*graph[i], end="\n")

# BFS 풀이
# from collections import deque
# import sys

# n = int(sys.stdin.readline())
# graph = [list(map(int, sys.stdin.readline().strip().split()))
#          for _ in range(n)]


# def bfs(start):
#     visit = [0] * n
#     q = deque()
#     q.append(start)

#     while q:
#         cur = q.popleft()

#         for i in range(n):
#             if graph[cur][i] == 1 and visit[i] == 0:
#                 visit[i] = 1
#                 q.append(i)

#     print(*visit, end="\n")


# for i in range(n):
#     bfs(i)
