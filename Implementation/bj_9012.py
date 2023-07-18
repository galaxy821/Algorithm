"""
괄호 [https://www.acmicpc.net/problem/9012]
"""

import sys


def is_vps(n):
    count = 0
    for i in n:
        if i == '(':
            count += 1
        elif i == ')':
            if count == 0:
                return "NO"
            else:
                count -= 1
    if count == 0:
        return "YES"
    else:
        return "NO"


for _ in range(int(sys.stdin.readline().strip())):
    input_string = sys.stdin.readline().strip()
    print(is_vps(input_string))
