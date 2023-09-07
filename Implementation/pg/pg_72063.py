"""
하노이의 탑 [https://school.programmers.co.kr/tryouts/72063/challenges?language=python3]
"""

result = []


def hanoi_tower(n, start, end, mid):
    if n == 1:
        result.append([start, end])
        return
    hanoi_tower(n-1, start, mid, end)
    result.append([start, end])
    hanoi_tower(n-1, mid, end, start)
    return


def solution(n):
    hanoi_tower(n, 1, 3, 2)
    return result


print(solution(7))
