"""
단지 번호 붙이기 [https://www.acmicpc.net/problem/2667]
"""

from collections import deque
import sys

move = [(0, -1), (0, 1), (1, 0), (-1, 0)]


def bfs(i, j):
    q = deque()
    q.append((i, j))
    board[i][j] = 0

    count = 1

    while q:
        cx, cy = q.popleft()

        for dx, dy in move:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
                board[nx][ny] = 0
                count += 1
                q.append((nx, ny))

    return count


n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

apart = 0
cnt_of_apart = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            apart += 1
            cnt_of_apart.append(bfs(i, j))

cnt_of_apart.sort()
print(apart, end="\n")
for i in cnt_of_apart:
    print(i, end="\n")
