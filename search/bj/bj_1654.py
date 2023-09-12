"""
랜선 자르기 [https://www.acmicpc.net/problem/1654]
"""
import sys

k, n = map(int, sys.stdin.readline().strip().split())
data = [int(sys.stdin.readline()) for _ in range(k)]

start = 1
end = max(data)

result = start

while start <= end:
    mid = start + (end - start)//2

    count = 0
    for line in data:
        count += (line // mid)

    if count >= n:
        start = mid + 1
        result = max(result, mid)
    else:
        end = mid - 1

print(result)
