"""
디스크 컨트롤러 [https://school.programmers.co.kr/tryouts/72096/challenges?language=python3]
"""

from heapq import heappush, heappop


def solution(jobs):
    answer = 0
    temp_time = -1
    cur_time = 0
    total_jobs = len(jobs)
    fin_jobs = 0

    q = []

    while fin_jobs < total_jobs:
        for job in jobs:
            if temp_time < job[0] <= cur_time:
                heappush(q, (job[1], job[0]))

        if len(q) > 0:
            cur = heappop(q)
            temp_time = cur_time
            cur_time += cur[0]
            answer += (cur_time - cur[1])
            fin_jobs += 1
        else:
            cur_time += 1

    return int(answer / len(jobs))


print(solution([[0, 3], [1, 9], [2, 6]]))  # 9
