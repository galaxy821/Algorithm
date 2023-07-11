"""
수열 정렬 [https://www.acmicpc.net/problem/1015]
"""

n = int(input())
data = list(map(int, input().split()))
result = list()

for i in range(len(data)):
    result.append([data[i], i])

result.sort(key=lambda x: (x[0], x[1]))

for i in range(len(result)):
    result[i][0] = i

result.sort(key=lambda x: (x[1], x[0]))
result = [x[0] for x in result]
print(*result)
