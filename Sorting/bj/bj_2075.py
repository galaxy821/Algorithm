"""
N번쨰 큰 수 [https://www.acmicpc.net/problem/2075]
"""

import heapq
import sys

n = int(sys.stdin.readline())
q = []

for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))

    for i in data:
        if len(q) == n:
            min_value = heapq.heappop(q)
            if min_value < i:
                heapq.heappush(q, i)
            else:
                heapq.heappush(q, min_value)
        else:
            heapq.heappush(q, i)

print(heapq.heappop(q))
