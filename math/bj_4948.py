"""
베르트랑 공준 [https://www.acmicpc.net/problem/4948]
"""

import sys
import math


def cal_prime(n):
    for i in range(2, int(math.sqrt(2*n))+1):
        if prime_data[i]:
            for j in range(i*2, 2*n+1, i):
                prime_data[j] = False


data = []

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    data.append(n)

prime_data = [True] * (2*max(data)+1)
prime_data[1] = False
cal_prime(max(data))

for i in data:
    count = 0
    for j in range(i+1, 2*i+1):
        if prime_data[j]:
            count += 1
    print(count, end="\n")
