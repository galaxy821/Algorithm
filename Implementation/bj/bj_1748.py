"""
수 이어 쓰기 [https://www.acmicpc.net/problem/1748]
"""
import sys
import math

n = sys.stdin.readline().strip()
num_len = len(n)
current_len = 1

anwser = 0
while True:
    if current_len == num_len:
        break
    anwser += int(math.pow(10, current_len) -
                  math.pow(10, current_len-1))*current_len
    current_len += 1

anwser += (int(int(n) % math.pow(10, current_len-1))+1)*current_len

print(anwser)
