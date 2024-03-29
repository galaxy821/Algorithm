"""
가장 긴 증가하는 부분 수열 [https://www.acmicpc.net/problem/11053]
"""

n = int(input())
data = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if data[j] < data[i]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))
