"""
강의실 배정
"""

from heapq import heappush, heappop
import sys

n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

data.sort(key=lambda x: (x[0], x[1]))

lecture = []
heappush(lecture, data[0][1])

for i in range(1, n):
    if lecture[0] > data[i][0]:
        heappush(lecture, data[i][1])
    else:
        heappop(lecture)
        heappush(lecture, data[i][1])

print(len(lecture))
