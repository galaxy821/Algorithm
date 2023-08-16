"""
토마토
"""

from collections import deque
import sys

dir = [[0, 0, 1], [0, 1, 0], [0, 0, -1], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]

m, n, h = map(int, sys.stdin.readline().strip().split())
data = [[list(map(int, sys.stdin.readline().strip().split()))
         for _ in range(n)] for _ in range(h)]

zero_count = 0
result = 0

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if data[i][j][k] == 1:
                q.append((i, j, k, 0))
            elif data[i][j][k] == 0:
                zero_count += 1

if zero_count == 0:
    print(result)
else:
    while q:
        l, x, y, day = q.popleft()

        result = day

        for dh, dx, dy in dir:
            nh, nx, ny = l + dh, x + dx, y + dy

            if 0 <= nh < h and 0 <= nx < n and 0 <= ny < m and data[nh][nx][ny] == 0:
                q.append((nh, nx, ny, day+1))
                data[nh][nx][ny] = 1
                zero_count -= 1
    if zero_count == 0:
        print(result)
    else:
        print(-1)
