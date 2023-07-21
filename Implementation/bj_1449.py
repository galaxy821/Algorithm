"""
수리공 항승 [https://www.acmicpc.net/problem/1449]
"""
import sys

num, length = sys.stdin.readline().split(" ")
values = list(map(int, sys.stdin.readline().split(" ")))
values.sort()

cur_pos = values[0] + length
count = 1

for i in range(1, num):
    if cur_pos < values[i] + 1:
        count += 1
        current = values[i] + length

print(count)
