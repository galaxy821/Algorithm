"""
이진 탐색 트리
"""

import sys
sys.setrecursionlimit(10**6)


def post_traversal(graph, start, end):
    if start > end:
        return

    mid = end + 1

    for i in range(start, mid):
        if graph[start] < graph[i]:
            mid = i
            break

    post_traversal(graph, start+1, mid-1)
    post_traversal(graph, mid, end)

    print(graph[start], end="\n")


graph = list(map(int, sys.stdin.readlines()))
post_traversal(graph, 0, len(graph)-1)
