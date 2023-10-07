"""
신고 결과 받기 [https://school.programmers.co.kr/tryouts/72128/challenges?language=python3]
"""

from collections import defaultdict

# 나의 풀이


def solution(id_list, report, k):
    data = defaultdict(set)
    report_list = defaultdict(set)

    for i in report:
        a, b = i.split()
        data[a].add(b)
        report_list[b].add(a)

    answer = []
    result_list = [key for key, value in report_list.items()
                   if len(value) >= k]
    for id in id_list:
        temp = 0
        for v in data[id]:
            if v in result_list:
                temp += 1

        answer.append(temp)

    return answer


# 효율적인 풀이
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported = {x: 0 for x in id_list}

    for r in set(report):
        a, b = r.split()
        reported[b] += 1

    for r in set(report):
        a, b = r.split()
        if reported[b] >= k:
            answer[id_list.index(a)] += 1

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], [
      "muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
