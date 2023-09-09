"""
올림픽 [https://www.acmicpc.net/problem/8979]
"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
print(n, k)

scores = list()
k_score = 0

for i in range(n):
    order, g, s, b = map(int, input().split())
    score = g*3+s*2+b
    if order == k:
        k_score = score
    scores.append(score)

scores = sorted(scores, reverse=True)
print(scores)

print(scores.index(k_score)+1)
