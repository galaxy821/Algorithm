"""
수 이어 쓰기 [https://www.acmicpc.net/problem/1748]
"""
import math

n = int(input())


def find_num(n):
    if n < 10:
        return n
    else:
        count = int(math.log10(n))
        low_max = pow(10, count)-1
        return (n - low_max) * (count+1) + find_num(low_max)


print(find_num(n))
