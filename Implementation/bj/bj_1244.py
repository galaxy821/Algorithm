"""
스위치 켜고 끄기 [https://www.acmicpc.net/problem/1244]
"""

import sys

n = int(sys.stdin.readline())
switch_data = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

for _ in range(m):
    sex, num = map(int, sys.stdin.readline().split())
    if sex == 1:
        for i in range(num-1, n, num):
            switch_data[i] = 1 if switch_data[i] == 0 else 0
    else:
        step = 1
        num -= 1
        switch_data[num] = 1 if switch_data[num] == 0 else 0
        while num - step >= 0 and num + step < n:
            if switch_data[num - step] == switch_data[num + step]:
                switch_data[num - step] = 1 if switch_data[num -
                                                           step] == 0 else 0
                switch_data[num + step] = 1 if switch_data[num +
                                                           step] == 0 else 0
            else:
                break
            step += 1

print(*switch_data)
