"""
연속합 [https://www.acmicpc.net/problem/1912]
"""

n = int(input())
data = list(map(int, input().split()))

dp = [0] * n
dp[0] = data[0]

for i in range(1, n):
    if dp[i-1] + data[i] > 0:
        dp[i] = max(dp[i-1] + data[i], data[i])
    else:
        dp[i] = data[i]

print(max(dp))
