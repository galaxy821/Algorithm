"""
색종이 [https://www.acmicpc.net/problem/2563]
"""

n = int(input())

board = [[0]*100 for _ in range(100)]

for _ in range(n):
    a, b = map(int, input().split())

    for i in range(a, a+10):
        for j in range(b, b+10):
            if board[i][j] == 0:
                board[i][j] = 1

print(sum([sum(x) for x in board]))
