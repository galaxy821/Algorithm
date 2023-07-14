"""
수 찾기 [https://www.acmicpc.net/problem/1920]
"""


def isExisting(num, data_set):
    if num in data_set:
        return 1
    else:
        return 0


n = int(input())
data_set = set(map(int, input().split()))
m = int(input())
find_list = [isExisting(x, data_set) for x in list(map(int, input().split()))]

for i in find_list:
    print(i, end="\n")
