"""
좌표 압축 [https://www.acmicpc.net/problem/18870]
"""

n = int(input())
data = list(zip([i for i in range(n)], list(map(int, input().split()))))
data.sort(key=lambda x: x[1])

index = 0
result = [[data[0][0], index]]
for i in range(1, n):
    if data[i-1][1] == data[i][1]:
        result.append([data[i][0], index])
    else:
        index += 1
        result.append([data[i][0], index])

result.sort(key=lambda x: x[0])

for x in result:
    print(x[1], end=" ")

# bisect 활용

# from bisect import bisect_left
# n = int(input())
# data = list(map(int, input().split()))
# set_data = list(set(data)).sort()

# for i in data :
#     print(bisect_left(set_data, i), end=" ")
