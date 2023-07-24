"""
미로 탐색 [https://www.acmicpc.net/problem/2178]
"""

from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split(" "))

board = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
q = deque()
q.append((0, 0, 1))
board[0][0] = 0

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = 1
while q:
    cx, cy, step = q.popleft()

    for dx, dy in dir:
        nx, ny = cx+dx, cy+dy

        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
            q.append((nx, ny, step+1))
            board[nx][ny] = 0
            if nx == n-1 and ny == m-1:
                result = step+1

print(result)
