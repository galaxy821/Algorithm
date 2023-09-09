"""
단어 정렬 [https://www.acmicpc.net/problem/1181]
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

values = set()
for i in range(int(input())):
    values.add(input())

values = sorted(values, key=lambda x: (len(x), x))
for value in values:
    print(value)
