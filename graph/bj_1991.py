"""
트리 순회
"""

import sys

sys.setrecursionlimit(10**6)


def prefix(node):
    if node == '.':
        return
    print(node, end="")
    prefix(tree[node][0])
    prefix(tree[node][1])


def midfix(node):
    if node == '.':
        return
    midfix(tree[node][0])
    print(node, end="")
    midfix(tree[node][1])


def postfix(node):
    if node == '.':
        return
    postfix(tree[node][0])
    postfix(tree[node][1])
    print(node, end="")


tree = {}
for _ in range(int(sys.stdin.readline())):
    node, left, right = sys.stdin.readline().strip().split()
    tree[node] = (left, right)

prefix("A")
print(end="\n")
midfix("A")
print(end="\n")
postfix("A")
print(end="\n")
