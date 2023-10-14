"""
유전법칙 [https://school.programmers.co.kr/tryouts/72138/challenges?language=python3]
"""


def cal_gene(pose):
    n, p = pose
    stack = []

    p -= 1
    while n > 1:
        stack.append(p % 4)
        n -= 1
        p //= 4

    while stack:
        num = stack.pop()
        if num == 0:
            return "RR"
        elif num == 3:
            return "rr"
    return "Rr"


def solution(queries):
    answer = []

    for query in queries:
        answer.append(cal_gene(query))

    return answer


print(solution([[3, 1], [2, 3], [3, 9]]))  # ["RR", "Rr", "RR"]
