"""
통계학 [https://www.acmicpc.net/problem/2108]
"""

import sys
from collections import Counter


def cal_mod(data):
    if (len(data) > 1):
        data_cnt = Counter(data)
        data_order = data_cnt.most_common()

        if data_order[0][1] == data_order[1][1]:
            return data_order[1][0]
        else:
            return data_order[0][0]
    else:
        return data[0]


data = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
data.sort()

data_avg = round(sum(data)/len(data))
data_mid = data[len(data)//2]
data_mod = cal_mod(data)
data_diff = max(data) - min(data)

print(data_avg, end="\n")
print(data_mid, end="\n")
print(data_mod, end="\n")
print(data_diff, end="\n")
