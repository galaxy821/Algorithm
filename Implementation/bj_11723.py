"""
집합 [https://www.acmicpc.net/problem/11723]
"""

import sys


def set_add(data, x):
    data.add(x)


def set_remove(data, x):
    data.discard(x)


def set_check(data, x):
    if x in data:
        return 1
    else:
        return 0


def set_toggle(data, x):
    if x in data:
        data.discard(x)
    else:
        data.add(x)


def set_all():
    return {i for i in range(1, 21)}


def set_empty():
    return set()


n = int(sys.stdin.readline())

data = set()

for _ in range(n):
    command = sys.stdin.readline().strip()
    if command == "all":
        data = set_all()
    elif command == "empty":
        data = set_empty()
    else:
        command, value = command.split(" ")
        if command == "add":
            set_add(data, int(value))
        elif command == "remove":
            set_remove(data, int(value))
        elif command == "check":
            print(set_check(data, int(value)))
        elif command == "toggle":
            set_toggle(data, int(value))
