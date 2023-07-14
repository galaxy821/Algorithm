"""
로프 [https://www.acmicpc.net/problem/2217]
"""

import sys

rope_list = list()
for i in range(int(sys.stdin.readline())):
    rope_list.append(int(sys.stdin.readline()))

rope_list.sort()
max_value = 0

for i in range(1, len(rope_list)+1):
    max_value = max(max_value, rope_list[len(rope_list)-i]*i)

print(max_value)
