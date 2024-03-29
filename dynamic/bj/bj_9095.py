"""
1,2,3 더하기 [https://www.acmicpc.net/problem/9095]
"""

import sys

dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print(dp[n], end='\n')
