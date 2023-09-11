"""
정수 삼각형 [https://www.acmicpc.net/problem/1932]
"""

import sys

n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            up_left = 0
        else:
            up_left = data[i-1][j-1]

        if j >= (len(data[i-1])):
            up_right = 0
        else:
            up_right = data[i-1][j]
        data[i][j] += max(up_left, up_right)

print(max(data[n-1]))
