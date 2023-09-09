"""
두 수의 합 [https://www.acmicpc.net/problem/3273]
"""

import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().strip().split()))
k = int(sys.stdin.readline())

data.sort()

front_index = 0
end_index = n-1
count = 0

while front_index < end_index:
    value = data[front_index] + data[end_index]
    if value == k:
        count += 1
        front_index += 1
    elif value > k:
        end_index -= 1
    else:
        front_index += 1

print(count)
