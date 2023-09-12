"""
순위 검색 [https://school.programmers.co.kr/tryouts/72077/challenges?language=python3]
"""

from collections import defaultdict
from itertools import combinations
from bisect import bisect_left


def solution(infos, queries):
    answer = []
    dic = defaultdict(list)

    for info in infos:
        info = info.split()
        condition = info[:-1]
        score = int(info[-1])

        for i in range(5):
            cases = list(combinations([0, 1, 2, 3], i))

            for case in cases:
                tmp = condition.copy()

                for i in case:
                    tmp[i] = "-"
                key = " ".join(tmp)
                dic[key].append(score)

    for d in dic.values():
        d.sort()

    for query in queries:
        query = query.replace("and ", "")
        query = query.split()

        key = query[:-1]
        key = ' '.join(key)
        score = int(query[-1])

        count = 0
        if key in dic:
            target_list = dic[key]
            idx = bisect_left(target_list, score)
            count = len(target_list) - idx
        answer.append(count)

    return answer


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], [
      "java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
