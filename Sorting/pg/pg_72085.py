"""
베스트 앨범 [https://school.programmers.co.kr/tryouts/72085/challenges?language=python3]
"""

from collections import defaultdict


def solution(genres, plays):
    n = len(genres)
    datas = defaultdict(list)
    total_plays = {}
    answer = []

    for i in range(n):
        datas[genres[i]].append((i, plays[i]))
        total_plays[genres[i]] = total_plays.get(genres[i], 0) + plays[i]

    sorted_tp = sorted(total_plays.items(), key=lambda x: -x[1])

    for key, data in datas.items():
        data.sort(key=lambda x: (-x[1], x[0]))

    for key, count in sorted_tp:
        for i in range(min(2, len(datas[key]))):
            answer.append(datas[key][i][0])

    return answer


print(solution(["classic", "pop", "classic",
      "classic", "pop"], [500, 600, 150, 800, 2500]))
