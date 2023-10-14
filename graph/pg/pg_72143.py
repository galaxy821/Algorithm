"""
보물 지도 [https://school.programmers.co.kr/tryouts/72143/challenges?language=python3]
"""

from collections import deque

d = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def solution(n, m, hole):
    answer = 0

    board = [[0] * m for _ in range(n)]
    for a, b in hole:
        board[a-1][b-1] = 1

    q = deque()
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]

    q.append((0, 0, False))
    visited[0][0][False] = True
    L = 0

    while q:
        for _ in range(len(q)):
            x, y, used = q.popleft()

            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][used] and board[nx][ny] == 0:
                    if (nx, ny) == (n-1, m-1):
                        return L + 1
                    visited[nx][ny][used] = True
                    q.append((nx, ny, used))
                if not used:
                    nx, ny = nx + dx, ny + dy
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][True] and board[nx][ny] == 0:
                        if (nx, ny) == (n-1, m-1):
                            return L + 1
                        visited[nx][ny][True] = True
                        q.append((nx, ny, True))
        L += 1

    return -1


print(solution(5, 4, [[1, 4], [2, 1], [2, 2], [2, 3],
      [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]))  # -1
