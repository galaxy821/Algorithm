"""
에라토스테네스의 체 [https://www.acmicpc.net/problem/2960]
"""

from collections import deque
import sys


def solution(n, k):  # solution with list of boolean type
    values = [True for i in range(n+1)]
    count = 0
    for i in range(2, n+1):
        if values[i]:
            for j in range(i, n+1, i):
                if values[j]:
                    values[j] = False
                    count += 1
                    if count == k:
                        return j


def solution2(n, k):  # solution with queue
    values = deque([i for i in range(2, n+1)])
    count = 0

    while count < k:
        cur_value = values.popleft()
        count += 1
        if count == k:
            return cur_value
        else:
            temp = cur_value
            cur_value = cur_value * 2
            while cur_value <= n:
                if cur_value in values:
                    values.remove(cur_value)
                    count += 1
                    if count == k:
                        return cur_value
                cur_value += temp


n, k = map(int, sys.stdin.readline().strip().split())

print(solution(n, k))
# print(solution2(n, k))
