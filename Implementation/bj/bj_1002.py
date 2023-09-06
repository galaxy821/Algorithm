"""
터렛 [https://www.acmicpc.net/problem/1002]
"""
import sys

for _ in range(int(sys.stdin.readline())):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().strip().split(" "))
    distance = pow((x2-x1), 2) + pow((y2-y1), 2)

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print("-1", end="\n")
        else:
            print("0", end="\n")
    elif distance < pow(r2-r1, 2):
        print("0", end="\n")
    elif distance == pow(r2-r1, 2):
        print("1", end="\n")
    elif distance == pow(r2+r1, 2):
        print("1", end="\n")
    elif distance > pow(r2+r1, 2):
        print("0", end="\n")
    else:
        print("2", end="\n")
