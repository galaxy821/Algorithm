"""
평범한 배낭
"""

import sys

n, k = map(int, sys.stdin.readline().strip().split())
data = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    weight, price = data[i-1]
    for j in range(1, k+1):
        if weight <= j:
            dp[i][j] = max(dp[i-1][j], price+dp[i-1][j-weight])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])
