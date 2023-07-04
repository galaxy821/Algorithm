"""
나이트 투어 [https://www.acmicpc.net/problem/1331]
"""

import sys

input = sys.stdin.readline

board = [[0]*6 for _ in range(6)]
row_values = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6}
move = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]

is_valid = True
start_position = input()
start_x, start_y = row_values[start_position[0]]-1, int(start_position[1])-1
cur_x, cur_y = start_x, start_y
board[cur_x][cur_y] = 1

for _ in range(35):
    position = input()
    if is_valid:
        n_x, n_y = row_values[position[0]]-1, int(position[1])-1
        if board[n_x][n_y] == 1:
            is_valid = False
        elif [n_x - cur_x, n_y - cur_y] not in move:
            is_valid = False
        else:
            board[n_x][n_y] = 1
            cur_x, cur_y = n_x, n_y

if [start_x - cur_x, start_y - cur_y] not in move:
    is_valid = False

if is_valid:
    print("Valid")
else:
    print("Invalid")
