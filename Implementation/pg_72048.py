"""
행렬 테두리 회전하기
"""


def solution(rows, columns, queries):
    answer = []
    board = []

    for i in range(rows):
        board.append([a for a in range(i*columns+1, (i+1)*columns+1)])

    print(board)
    for query in queries:
        x1, y1, x2, y2 = query
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        temp_value = board[x1][y1]
        values = []
        values.append(temp_value)

        for i in range(x1+1, x2+1):
            print(i)
            board[i-1][y1] = board[i][y1]
            values.append(board[i-1][y1])

        for i in range(y1+1, y2+1):
            board[x2][i-1] = board[x2][i]
            values.append(board[x2][i-1])

        for i in range(x2-1, x1-1, -1):
            board[i+1][y2] = board[i][y2]
            values.append(board[i+1][y2])

        for i in range(y2-1, y1, -1):
            board[x1][i+1] = board[x1][i]
            values.append(board[x1][i+1])

        board[x1][y1+1] = temp_value
        answer.append(min(values))
    return answer


print(solution(100, 97, [[1, 1, 100, 97]]))
