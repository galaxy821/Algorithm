"""
구명보트 [https://school.programmers.co.kr/tryouts/72123/challenges?language=python3]
"""


def solution(people, limit):
    people.sort()
    answer = 0

    s, e = 0, len(people)-1

    while s < e:
        if people[s] + people[e] <= limit:
            s += 1
            e -= 1
            answer += 1
        else:
            e -= 1

    return len(people)-answer


print(solution([70, 50, 80, 50], 100))  # 3
