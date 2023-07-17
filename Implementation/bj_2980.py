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
    app_time = position - cur_position

    if app_time < red_time:
        duration += (app_time + red_time)
    elif app_time < (red_time + blue_time):
        duration += app_time
    else:
        left_time = app_time % (red_time + blue_time)
        if left_time < red_time:
            duration += app_time + (red_time+left_time)
        else:
            duration += app_time
    print(app_time, cur_position, duration)
    cur_position = position

duration += length - cur_position
print(cur_position, duration)
print(duration)
