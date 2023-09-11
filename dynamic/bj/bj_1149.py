"""
RGB 거리 [https://www.acmicpc.net/problem/1149]
"""

import sys

n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

dp = [[0, 0, 0] for _ in range(n)]
dp[0][0], dp[0][1], dp[0][2] = data[0][0], data[0][1], data[0][2]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + data[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + data[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + data[i][2]

print(min(dp[n-1]))
