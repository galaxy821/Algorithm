"""
평균 [https://www.acmicpc.net/problem/1546]
"""

n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)

new_total_score = 0

for score in scores:
    new_total_score += (score / max_score * 100)

print(new_total_score/n)
