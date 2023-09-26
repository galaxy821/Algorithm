"""
30 [https://www.acmicpc.net/problem/10610]
"""

n = list(map(int, input()))

if sum(n) % 3 == 0 and 0 in n:
    n.sort(reverse=True)
    print("".join(map(str, n)))
else:
    print(-1)
