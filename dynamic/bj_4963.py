"""
섬의 개수 [https://www.acmicpc.net/problem/4963]
"""
import sys
from collections import deque

dir = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
board = []


def cal_island(visit, x, y, w, h):
    q = deque()
    q.append([x, y])
    visit[x][y] = 0

    while q:
        temp = q.popleft()
        for dx, dy in dir:
            nx, ny = temp[0] + dx, temp[1] + dy
            if 0 <= nx < h and 0 <= ny < w and visit[nx][ny] == 1:
                q.append([nx, ny])
                visit[nx][ny] = 0
    return


while True:
    w, h = map(int, sys.stdin.readline().strip().split(" "))
    if w == 0 and h == 0:
        break

    if w == 1:
        board = [[int(sys.stdin.readline())] for _ in range(h)]
    else:
        board = [list(map(int, sys.stdin.readline().strip().split(" ")))
                 for _ in range(h)]

    result = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                cal_island(board, i, j, w, h)
                result += 1

    print(result, end="\n")
