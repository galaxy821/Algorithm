"""
겹치는 선분 [https://www.acmicpc.net/problem/1689]
"""

from heapq import heappush, heappop
import sys

n = int(sys.stdin.readline())
line = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

line.sort(key=lambda x: (x[0], x[1]))

heap = []
heappush(heap, line[0][1])
result = 1

for s, e in line[1:]:
    while heap and heap[0] <= s:
        heappop(heap)
    heappush(heap, e)
    result = max(result, len(heap))

print(result)
