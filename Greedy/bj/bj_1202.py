"""
보석 도둑 [https://www.acmicpc.net/problem/1202]
"""

import sys
import heapq
input = sys.stdin.readline
n, k = map(int, input().split())
gems = [[*map(int, input().split())] for _ in range(n)]
bags = [int(input()) for _ in range(k)]
gems.sort()
bags.sort()
result = 0
tmp = []

for bag in bags:
    while gems and gems[0][0] <= bag:
        heapq.heappush(tmp, -gems[0][1])
        heapq.heappop(gems)
    if tmp:
        result -= heapq.heappop(tmp)
print(result)
