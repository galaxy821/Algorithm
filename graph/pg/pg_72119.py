"""
게임 맵 최단 거리 [https://school.programmers.co.kr/tryouts/72119/challenges?language=python3]
"""

from collections import deque

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def solution(maps):
    answer = int(1e10)

    n = len(maps)
    m = len(maps[0])

    visited = [[False]*(m+1) for _ in range(n+1)]

    q = deque()
    q.append((1, 1, 1))
    visited[1][1] = True

    while q:
        print(q)
        cx, cy, step = q.popleft()

        if cx == n and cy == m:
            answer = min(answer, step)

        for dx, dy in dir:
            nx, ny = cx + dx, cy + dy
            if 0 < nx <= n and 0 < ny <= m and maps[nx-1][ny-1] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, step+1))

    if answer == int(1e10):
        return -1
    else:
        return answer


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
      1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))  # 11
