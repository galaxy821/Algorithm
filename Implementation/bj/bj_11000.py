"""
강의실 배정 [https://www.acmicpc.net/problem/11000]
"""

from heapq import heappush, heappop
import sys

n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().rstrip().split()))
        for _ in range(n)]
data.sort(key=lambda x: (x[0], x[1]))

heap = []
heappush(heap, data[0][1])

for i in range(1, n):
    if heap[0] > data[i][0]:
        heappush(heap, data[i][1])
    else:
        heappop(heap)
        heappush(heap, data[i][1])

print(len(heap))
