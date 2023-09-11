"""
A -> B [https://www.acmicpc.net/problem/16953]
"""

from collections import deque

a, b = map(int, input().split())

q = deque()
q.append((a, 1))

result = 1e9

while q:
    cur, cnt = q.popleft()

    if cur == b:
        result = min(result, cnt)

    if cur*2 <= b:
        q.append((cur*2, cnt+1))

    if cur*10+1 <= b:
        q.append((cur*10+1, cnt+1))


if result == 1e9:
    print("-1")
else:
    print(result)
