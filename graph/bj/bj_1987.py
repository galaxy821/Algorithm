"""
알파벳 [https://www.acmicpc.net/problem/1987]
"""

import sys

sys.setrecursionlimit(10**9)

N, K = map(int, input().split())
board = list()
visited = set()
count = 0
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(N):
    board.append(list(input()))


def dfs(x, y, answer):
    global count
    count = max(count, answer)

    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < K and board[nx][ny] not in visited:
            visited.add(board[nx][ny])
            dfs(nx, ny, answer+1)
            visited.remove(board[nx][ny])


visited.add(board[0][0])
dfs(0, 0, 1)
print(count)
