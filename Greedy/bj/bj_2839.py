# baekjooon 2839
n = int(input())
sugar = [5, 3]
result = 10e9

for count in range(n//sugar[0]+1):
    left = n - count*sugar[0]
    if left % sugar[1] == 0:
        result = min(result, count + left//sugar[1])

if (result == 10e9):
    print(-1)
else:
    print(result)

# dynamic programming

# n = int(input())
# dp = [5001] * (n+1)
# dp[0] = 0
# for k in [3, 5]:
#     for i in range(k, n+1):
#         dp[i] = min(dp[i], dp[i-k]+1)

# if dp[n] != 5001:
#     print(dp[n])
# else:
#     print(-1)
