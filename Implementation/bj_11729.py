"""
하노이 탑 이동 순서
"""

n = int(input())


def tower_hanoi(n, start, end, mid):
    if n == 1:
        print(start, end, end="\n")
        return
    tower_hanoi(n-1, start, mid, end)
    print(start, end, end="\n")
    tower_hanoi(n-1, mid, end, start)


print(2**n-1, end="\n")
tower_hanoi(n, 1, 3, 2)
