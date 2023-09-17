"""
등굣길 [https://school.programmers.co.kr/tryouts/72089/challenges]
"""


def solution(m, n, puddles):

    dp = [[0]*(n+1) for _ in range(m+1)]

    dp[1][1] = 1

    for i in range(1, m+1):
        for j in range(1, n+1):
            if i == 1 and j == 1:
                continue
            if [i, j] not in puddles:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007

    return dp[m][n]


print(solution(4, 3, [[2, 2]]))
