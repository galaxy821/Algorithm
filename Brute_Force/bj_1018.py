"""
체스판 다시 칠하기 [https://www.acmicpc.net/problem/1018]
"""

h, w = map(int, input().split())
board = [list(input().split()) for _ in range(h)]
result = h * w

for i in range(h-7):
    for j in range(w-7):
        w_count = 0
        b_count = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'W':
                        w_count += 1
                    else:
                        b_count += 1
                else:
                    if board[a][b] != 'B':
                        w_count += 1
                    else:
                        b_count += 1

        result = min(result, b_count, w_count)
print(result)
