"""
선 그리기 [https://www.acmicpc.net/problem/16396]
"""

n = int(input())

line_state = [0] * 10001

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, b):
        if line_state[i] == 0:
            line_state[i] = 1

print(sum(line_state))
