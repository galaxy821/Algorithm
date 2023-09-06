"""
요세푸스 문제 0 [https://www.acmicpc.net/problem/11866]
"""

from collections import deque

n, k = map(int, input().split())

data = deque([i for i in range(1, n+1)])
result = list()

while data:
    for _ in range(k-1):
        data.append(data.popleft())
    result.append(data.popleft())

print("<"+", ".join(map(str, result))+">")
