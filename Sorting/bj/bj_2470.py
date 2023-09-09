"""
두 용액
"""

n = int(input())

data = list(map(int, input().split()))
data.sort()

start = 0
end = n-1

min_value = data[start] + data[end]
result = [data[start], data[end]]

while start < end:
    value = data[start] + data[end]

    if abs(value) < abs(min_value):
        min_value = abs(value)
        result = [data[start], data[end]]

    if value < 0:
        start += 1
    else:
        end -= 1

print(result[0], result[1])
