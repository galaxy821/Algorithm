"""
파도반 수열 [https://www.acmicpc.net/problem/9461]
"""

import sys

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, 101):
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print(dp[n], end="\n")
