"""
경주로 건설 [https://school.programmers.co.kr/tryouts/72120/challenges?language=python3]
"""

from heapq import heappush, heappop
from sys import maxsize

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
nd = len(d)


def solution(board):
    N = len(board)
    costboard = [[[maxsize] * N for _ in range(N)] for _ in range(4)]

    for i in range(4):
        costboard[i][0][0] = 0

    heap = [(0, 0, 0, 0), (0, 0, 0, 1)]

    while heap:
        cost, cx, cy, cd = heappop(heap)

        for i in range(nd):
            nx, ny = cx + d[i][0], cy + d[i][1]

            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                ncost = cost + (100 if cd == i else 600)

                if costboard[i][nx][ny] > ncost:
                    costboard[i][nx][ny] = ncost
                    heappush(heap, (ncost, nx, ny, i))

    return min(costboard[0][N-1][N-1], costboard[1][N-1][N-1], costboard[2][N-1][N-1], costboard[3][N-1][N-1])


print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [
      1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]))  # 3200
