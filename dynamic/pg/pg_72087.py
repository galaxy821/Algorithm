"""
N으로 표현 [https://school.programmers.co.kr/tryouts/72087/challenges]
"""


def solution(N, number):
    answer = -1

    dp = []

    for i in range(1, 9):
        num_of_set = set()
        num_of_set.add(int(str(N)*i))

        for j in range(0, i-1):
            for op1 in dp[j]:
                for op2 in dp[-j-1]:
                    num_of_set.add(op1 + op2)
                    num_of_set.add(op1 - op2)
                    num_of_set.add(op1 * op2)
                    if op2 != 0:
                        num_of_set.add(op1 // op2)

        if number in num_of_set:
            return i

        dp.append(num_of_set)

    return answer


print(solution(5, 12))
