"""
기타줄 [https://www.acmicpc.net/problem/1049]
"""
import sys

n, m = map(int, sys.stdin.readline().split())
list_cost = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

package_cost = [i[0] for i in sorted(list_cost, key=lambda x: x[0])]
single_cost = [i[1] for i in sorted(list_cost, key=lambda x: x[1])]

total_cost = 0

if package_cost[0] < single_cost[0] * 6:
    total_cost = package_cost[0] * (n // 6)

    if package_cost[0] < single_cost[0] * (n % 6):
        total_cost += package_cost[0]
    else:
        total_cost += single_cost[0] * (n % 6)
else:
    total_cost = single_cost[0] * n

print(total_cost)
