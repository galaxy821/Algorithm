"""
모의고사 [https://school.programmers.co.kr/tryouts/72067/challenges?language=python3]
"""


student1 = [1, 2, 3, 4, 5]
student2 = [2, 1, 2, 3, 2, 4, 2, 5]
student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]


def solution(answers):
    answer = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == student1[i % 5]:
            answer[0] += 1
        if answers[i] == student2[i % 8]:
            answer[1] += 1
        if answers[i] == student3[i % 10]:
            answer[2] += 1

    result = []
    max_value = max(answer)
    if max_value == answer[0]:
        result.append(1)
    if max_value == answer[1]:
        result.append(2)
    if max_value == answer[2]:
        result.append(3)

    return result


print(solution([1, 3, 2, 4, 2]))
