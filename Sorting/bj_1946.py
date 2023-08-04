"""
신입 사원 [https://www.acmicpc.net/problem/1946]
"""

import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())

    data = [list(map(int, sys.stdin.readline().strip().split()))
            for _ in range(n)]
    data.sort()

    result = 1

    max_value = data[0][1]
    for i in range(len(data)):
        if max_value > data[i][1]:
            result += 1
            max_value = data[i][1]

    print(result)
