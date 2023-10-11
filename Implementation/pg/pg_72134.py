"""
파괴되지 않은 건물 [https://school.programmers.co.kr/tryouts/72134/challenges?language=python3]
"""


def solution(board, skill):
    answer = 0

    temp = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]

    for typ, r1, c1, r2, c2, degree in skill:
        temp[r1][c1] += degree if typ == 2 else -degree
        temp[r1][c2 + 1] += -degree if typ == 2 else degree
        temp[r2 + 1][c1] += -degree if typ == 2 else degree
        temp[r2 + 1][c2 + 1] += degree if typ == 2 else -degree

    for i in range(len(temp)-1):
        for j in range(len(temp[0])-1):
            temp[i][j + 1] += temp[i][j]

    for j in range(len(temp[0])-1):
        for i in range(len(temp)-1):
            temp[i + 1][j] += temp[i][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += temp[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [
      [1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))  # 10
