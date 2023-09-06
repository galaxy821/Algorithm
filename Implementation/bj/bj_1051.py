"""
숫자 정사작형 [https://www.acmicpc.net/problem/1051]
"""
import sys
n, m = map(int, sys.stdin.readline().split(" "))
board = [list(map(int, sys.stdin.readline().strip()))
         for _ in range(n)]

max_value = 0
size = 0

for length in range(min(n, m)):
    for i in range(n-length):
        for j in range(m-length):
            if board[i][j] == board[i+length][j] and board[i][j] == board[i][j+length] and board[i][j] == board[i+length][j+length]:
                max_value = max(max_value, board[i][j])
                size = length

print((size+1)**2)
