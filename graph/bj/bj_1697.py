"""
숨바꼭질 [https://www.acmicpc.net/problem/1697]
"""

from collections import deque

LIMIT = 100001

n, k = map(int, input().split())

q = deque()
q.append((n, 0))
visit = [False] * LIMIT
result = LIMIT

visit[n] = True

while q:
    cur, step = q.popleft()
    if cur == k:
        result = step
        break

    if cur * 2 < LIMIT and not visit[cur*2]:
        q.append((cur*2, step+1))
        visit[cur*2] = True
    if cur+1 < LIMIT and not visit[cur+1]:
        q.append((cur+1, step+1))
        visit[cur+1] = True
    if cur-1 >= 0 and not visit[cur-1]:
        q.append((cur-1, step+1))
        visit[cur-1] = True

print(result)
