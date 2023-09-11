"""
정수 삼각형 [https://school.programmers.co.kr/learn/courses/30/lessons/43105]
"""


def solution(triangle):
    length = len(triangle)

    table = [[0]*i for i in range(1, length+1)]

    table[0][0] = triangle[0][0]

    for i in range(1, length):
        for j in range(0, i+1):
            if j == 0:
                table[i][j] = table[i-1][j] + triangle[i][j]
            elif j == i:
                table[i][j] = table[i-1][j-1] + triangle[i][j]
            else:
                table[i][j] = max(table[i-1][j], table[i-1]
                                  [j-1]) + triangle[i][j]

    return max(table[length-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
