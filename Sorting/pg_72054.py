"""
튜플 [https://school.programmers.co.kr/tryouts/72054/challenges?language=python3]
"""

# 정렬 후 문자열을 잘 다루어야 하는 문제


def solution(s):
    list_of_sets = list(s[2:-2].split("},{"))

    list_of_sets.sort(key=lambda x: len(x))

    answer = []
    num = set()

    for i in list_of_sets:
        data = list(map(int, i.split(",")))

        for j in data:
            if not j in num:
                num.add(j)
                answer.append(j)

    return answer


print(solution("{{123}}"))
