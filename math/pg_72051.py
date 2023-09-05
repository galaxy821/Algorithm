"""
행렬의 곱셈 [https://school.programmers.co.kr/tryouts/72051/challenges?language=python3]
"""

# 흔한 2차원 행렬 곱셈 문제


def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for k in range(len(arr2[0])):
            sum = 0
            for j in range(len(arr2)):
                sum += arr1[i][j] * arr2[j][k]
            answer[i][k] = sum

    return answer


# output : [[15, 15], [15, 15], [15, 15]]
print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
