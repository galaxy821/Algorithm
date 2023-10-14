"""
운영체제 [https://school.programmers.co.kr/tryouts/72139/challenges?language=python3]
"""

from heapq import heappush, heappop


def solution(program):
    answer = [0] * 11
    heap = []

    program.sort(key=lambda x: (x[1], x[0]))

    time = 0

    while program or heap:
        while program and program[0][1] <= time:
            heappush(heap, program.pop(0))

        if program and not heap:
            time = program[0][1]
            heappush(heap, program.pop(0))

        temp = heappop(heap)

        answer[temp[0]] += (time - temp[1])
        time += temp[2]

    answer[0] = time

    return answer


# [20, 5, 0, 16, 0, 0, 0, 0, 0, 0, 0]
print(solution([[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]))
