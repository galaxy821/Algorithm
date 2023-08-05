"""
회의실 배정 [https://www.acmicpc.net/problem/1931]
"""

import sys

n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
data.sort(key=lambda x: (x[1], x[0]))

end_time = data[0][1]
result = 1

for i in range(1, n):
    if end_time <= data[i][0]:
        end_time = data[i][1]
        result += 1

print(result)
