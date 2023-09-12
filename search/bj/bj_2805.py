"""
나무 자르기 [https://www.acmicpc.net/problem/2805]
"""

n, m = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = max(data)
result = 0

while start <= end:
    mid = start + (end - start)//2

    value = 0
    for i in data:
        if i > mid:
            value += (i - mid)

    if value >= m:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)
