"""
시리얼 번호 [https://www.acmicpc.net/problem/1431]
"""

import sys


def sum_value(value):
    return sum([int(i) for i in value if i.isdigit()])


values = []
for _ in range(int(sys.stdin.readline())):
    values.append(sys.stdin.readline().strip())

values.sort(key=lambda x: (len(x), sum_value(x), x))

for value in values:
    print(value, end="\n")
