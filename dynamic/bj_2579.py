"""
계단 오르기 [https://www.acmicpc.net/problem/2579]
"""

import sys

n = int(sys.stdin.readline())
scores = [int(sys.stdin.readline()) for _ in range(n)]

dp = [[0, 0] for _ in range(n+1)]
dp[1] = [scores[0], 0]

for i in range(2, n+1):
    dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + scores[i-1]
    dp[i][1] = dp[i-1][0] + scores[i-1]

print(max(dp[n][0], dp[n][1]))
