"""
2xn 타일링 [https://www.acmicpc.net/problem/11726]
"""
n = int(input())

dp = [1] * (n+1)

if n != 1:
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])
