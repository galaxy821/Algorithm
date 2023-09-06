"""
킹 [https://www.acmicpc.net/problem/1063]
"""

import sys

direction = {
    "R": (1, 0),
    "L": (-1, 0),
    "B": (0, -1),
    "T": (0, 1),
    "RT": (1, 1),
    "LT": (-1, 1),
    "RB": (1, -1),
    "LB": (-1, -1)

}

king, stone, n = sys.stdin.readline().strip().split(" ")
board = [[0 for j in range(8)] for i in range(8)]
kx, ky = ord(king[0])-65, int(king[1]) - 1
sx, sy = ord(stone[0])-65, int(stone[1])-1

for _ in range(int(n)):
    cx, cy = direction[sys.stdin.readline().strip()]
    nx, ny = kx + cx, ky + cy
    if 0 <= nx < 8 and 0 <= ny < 8:
        if nx == sx and ny == sy:
            s_nx, s_ny = sx + cx, sy + cy

            if 0 <= s_nx < 8 and 0 <= s_ny < 8:
                sx, sy = s_nx, s_ny
                kx, ky = nx, ny
        else:
            kx, ky = nx, ny

print(chr(kx+65)+str(ky+1))
print(chr(sx+65)+str(sy+1))
