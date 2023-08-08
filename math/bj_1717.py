"""
집합의 표현
"""

import sys
sys.setrecursionlimit(10**6)


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, sys.stdin.readline().strip().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    op, a, b = map(int, sys.stdin.readline().strip().split())
    if op == 0:
        union_parent(parent, a, b)
    elif op == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES", end="\n")
        else:
            print("NO", end="\n")
