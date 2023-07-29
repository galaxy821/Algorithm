"""
병사 배치하기 [https://www.acmicpc.net/problem/18353]
"""

n = int(input())
data = list(map(int, input().split()))

dp = [1]*n

for i in range(1, n):
    for j in range(0, i):
        if data[j] > data[i]:
            dp[i] = max(dp[j]+1, dp[i])

print(n-max(dp))
