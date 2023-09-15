"""
위장 [https://school.programmers.co.kr/tryouts/72083/challenges?language=python3]
"""


def solution(clothes):
    dic = {}

    for cloth, t in clothes:
        dic[t] = dic.get(t, 0) + 1

    answer = 1
    for t in dic:
        answer *= (dic[t] + 1)

    return answer - 1


print(solution([["crow_mask", "face"], [
      "blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
