"""
안테나 [https://www.acmicpc.net/problem/18310]
"""

n = int(input())
values = list(map(int, input().split())).sort()

print(values[(len(values)-1) // 2])
