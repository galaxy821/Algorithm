"""
퇴사 [https://www.acmicpc.net/problem/14501]
"""

import sys

n = int(sys.stdin.readline())
values = [tuple(map(int, sys.stdin.readline().strip().split(" ")))
          for _ in range(n)]

dp = [0] * (n+1)
result = 0

for i in range(n-1, -1, -1):
    if values[i][0] + i <= n:
        dp[i] = max(result, values[i][1] + dp[i+values[i][0]])
        result = max(result, dp[i])
    else:
        dp[i] = result


print(dp[0])
