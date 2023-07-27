"""
섬의 개수 [https://www.acmicpc.net/problem/4963]
"""
from collections import deque
import sys

dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def bfs(board, n, m):
    q = deque()
    q.append((n, m))
    board[n][m] = 0

    while q:
        cx, cy = q.popleft()

        for dx, dy in dir:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(board) and 0 <= ny < len(board[n]) and board[nx][ny] == 1:
                q.append((nx, ny))
                board[nx][ny] = 0


while True:
    n, m = map(int, sys.stdin.readline().strip().split())
    if n == 0 and m == 0:
        break
    board = [list(map(int, sys.stdin.readline().strip().split()))
             for _ in range(m)]

    count = 0
    for x in range(m):
        for y in range(n):
            if board[x][y] == 1:
                bfs(board, x, y)
                count += 1

    print(count, end="\n")
