"""
1로 만들기 [https://www.acmicpc.net/problem/1463]
"""

n = int(input())

if n == 1:
    print("0")
elif n == 2:
    print("1")
elif n == 3:
    print("1")
else:
    dp = [0]*(n+1)
    dp[2] = 1
    dp[3] = 1
    for i in range(4, n+1):
        dp[i] = dp[i-1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2]+1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3]+1)

    print(dp[n])
