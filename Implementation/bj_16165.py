"""
걸그룹 마스터 준석이 [https://www.acmicpc.net/problem/16165]
"""

import sys

n, m = map(int, sys.stdin.readline().strip().split())
data = {}

for _ in range(n):
    name = sys.stdin.readline().strip()

    data[name] = set()
    for _ in range(int(sys.stdin.readline())):
        data[name].add(sys.stdin.readline().strip())

for _ in range(m):
    name = sys.stdin.readline().strip()
    num_type = int(sys.stdin.readline())

    if num_type == 1:
        for key in data.keys():
            if name in data[key]:
                print(key, end="\n")
                break
    else:
        for value in sorted(data[name]):
            print(value, end="\n")
