"""
기타레슨 [https://www.acmicpc.net/problem/2343]
"""

n, k = map(int, input().split())
values = list(map(int, input().split()))

start = 1
end = int(1e10)
result = int(1e10)
max_value = max(values)

while start <= end:
    mid = start + (end - start)//2

    if mid < max_value:
        start = mid + 1
        continue

    count = 1
    temp = 0
    for value in values:
        if temp + value <= mid:
            temp += value
        else:
            count += 1
            temp = value

    if count <= k:
        end = mid-1
        result = mid
    else:
        start = mid+1
print(result)
