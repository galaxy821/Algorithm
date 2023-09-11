"""
동전 1
"""

import sys

n, k = map(int, sys.stdin.readline().strip().split())

coins = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0 for i in range(k+1)]

for coin in coins:
    if coin > k:
        continue

    dp[coin] += 1

    for i in range(coin+1, k+1):
        if dp[i-coin] > 0:
            dp[i] += dp[i-coin]

    print(dp)
print(dp[k])
