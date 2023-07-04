"""
나이트 투어 [https://www.acmicpc.net/problem/1331]
"""

import sys

input = sys.stdin.readline

board = [[0]*6 for _ in range(6)]
row_values = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6}

is_valid = True
for _ in range(36):
    position = input()
    if board[row_values[position[0]]-1][int(position[1])-1] == 1:
        is_valid = False
    else:
        board[row_values[position[0]]-1][int(position[1])-1] = 1

if is_valid:
    print("Valid")
else:
    print("Invalid")
