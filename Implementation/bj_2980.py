"""
도로와 신호등 [https://www.acmicpc.net/problem/2980]
"""
from collections import deque
import sys

num, length = map(int, sys.stdin.readline().strip().split())

duration = 0
cur_position = 0

for _ in range(num):
    position, red_time, blue_time = map(
        int, sys.stdin.readline().strip().split())
    duration += (position - cur_position)

    left_time = duration % (red_time + blue_time)
    if left_time < red_time:
        duration += (red_time-left_time)
    else:
        cur_position += (left_time-red_time)
    cur_position += (position - cur_position)

duration += length - cur_position
print(duration)
