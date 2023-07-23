"""
예산 [https://www.acmicpc.net/problem/2512]
"""

import sys

n = int(sys.stdin.readline())
costs = list(map(int, sys.stdin.readline().strip()))
max_cost = int(sys.stdin.readline())

start = min(costs)
end = max(costs)

result = max_cost // n
while start <= end:
    mid = start + (end - start) // 2
    value = 0

    for cost in costs:
        if cost <= mid:
            value += cost
        else:
            value += mid

    if value >= max_cost:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
