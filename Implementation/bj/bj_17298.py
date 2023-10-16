"""
오큰수 [https://www.acmicpc.net/problem/17298]
"""

from collections import deque

n = int(input())
data = list(map(int, input().split()))

result = [-1] * n
stack = deque()

# for i in range(n):
#     while stack and data[i] > stack[-1][0]:
#         temp, idx = stack.pop()
#         result[idx] = data[i]
#     stack.append((data[i], i))

for i in range(n):
    while stack and data[i] > data[stack[-1]]:
        result[stack.pop()] = data[i]
    stack.append(i)

print(*result)
