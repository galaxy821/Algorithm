"""
주유소 [https://www.acmicpc.net/problem/13305]
"""

import sys

n = int(input())
dist = list(map(int, sys.stdin.readline().strip().split()))
cost = list(map(int, sys.stdin.readline().strip().split()))

array = [[0, 0] for _ in range(n-1)]
array[n-2][0] = cost[n-2]
array[n-2][1] = dist[n-2]
for i in range(n-3, -1, -1):
    array[i][0] = cost[i]
    array[i][1] = dist[i] + array[i+1][1]

array.sort()
current_dist = 0
result = 0
for i in range(n-1):
    if current_dist < array[i][1]:
        result += (array[i][1] - current_dist) * array[i][0]
        current_dist = array[i][1]
print(result)
