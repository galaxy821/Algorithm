"""
완주하지 못한 선수 [https://school.programmers.co.kr/tryouts/72081/challenges?language=python3]
"""


def solution(participant, completion):

    dic = {}
    for x in participant:
        dic[x] = dic.get(x, 0) + 1
    for x in completion:
        dic[x] -= 1

    answer = [k for k, v in dic.items() if v > 0][0]

    return answer
