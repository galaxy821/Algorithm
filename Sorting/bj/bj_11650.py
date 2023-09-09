"""
좌표 정렬하기 [https://www.acmicpc.net/problem/11650]
"""
import sys

n = int(sys.stdin.readline())

values = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
values = sorted(values, key=lambda x: (x[0], x[1]))

for i in range(n):
    sys.stdout.write(f"{values[i][0]} {values[i][1]}\n")
