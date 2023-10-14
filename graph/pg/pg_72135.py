"""

"""

# import sys


# sys.setrecursionlimit(10**9)
# d = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# def solution(board, aloc, bloc):

#     def dfs(x1, y1, x2, y2, board, count):
#         count_list = []

#         if board[x1][y1] == 0:
#             return count

#         board[x1][y1] = 0

#         temp = 0

#         for dx, dy in d:
#             nx, ny = x1 + dx, y1 + dy

#             if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 1:

#                 count_list.append(dfs(x2, y2, nx, ny, board, count+1))

#             else:
#                 temp += 1

#         if temp == 4 and count < answer:
#             answer = count

#         return max(count_list)

#     answer = dfs(aloc[0], aloc[1], bloc[0], bloc[1], board, 0)

#     return answer


import sys

sys.setrecursionlimit(10**9)
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
INF = 987654321


def in_range(board, x, y):
    if 0 <= x < len(board) and 0 <= y < len(board[0]):
        return True
    return False


def is_finished(board, x, y):
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if in_range(board, nx, ny) and board[nx][ny]:
            return False
    return True


def solve(board, x1, y1, x2, y2):
    if is_finished(board, x1, y1):
        return [False, 0]

    if x1 == x2 and y1 == y2:
        return [True, 1]

    min_turn = INF
    max_turn = 0
    can_win = False

    for dx, dy in d:

        nx, ny = x1 + dx, y1 + dy
        if not in_range(board, nx, ny) or not board[nx][ny]:
            continue
        board[x1][y1] = 0
        result = solve(board, x2, y2, nx, ny)
        board[x2][y2] = 1

        if not result[0]:
            can_win = True
            min_turn = min(min_turn, result[1])
        elif not can_win:
            max_turn = max(max_turn, result[1])

    turn = min_turn if can_win else max_turn

    return [can_win, turn + 1]


def solution(board, aloc, bloc):

    return solve(board, aloc[0], aloc[1], bloc[0], bloc[1])[1]


print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))  # 5
