"""
최댓값 [https://www.acmicpc.net/problem/2562]
"""

max_value = -1
index = -1
for i in range(9):
    temp = int(input())
    if max_value < temp :
        max_value = temp
        index = i
print(max_value, index+1, sep="\n")

## 다른 풀이
"""
values = list()
for _ in range(9):
    values.append(int(input()))
print(max(values))
print(values.index(max(values))+1)
"""