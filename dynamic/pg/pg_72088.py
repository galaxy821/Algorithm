"""
정수 삼각형 [https://school.programmers.co.kr/tryouts/72088/challenges]
"""


def solution(triangle):

    dp = [[0] * (i+1) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i-1][j]
            elif j == i:
                dp[i][j] = triangle[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = triangle[i][j] + max(dp[i-1][j], dp[i-1][j-1])

    return max(dp[len(triangle)-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))  # 30
