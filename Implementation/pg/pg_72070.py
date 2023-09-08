"""
불량 사용자 [https://school.programmers.co.kr/tryouts/72070/challenges?language=python3]
"""
# 성공한 풀이
from functools import reduce
from itertools import permutations


def check(case, banned_id):
    for i in range(len(banned_id)):
        if len(case[i]) != len(banned_id[i]):
            return False
        for j in range(len(case[i])):
            if banned_id[i][j] == "*":
                continue
            elif case[i][j] != banned_id[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    ban_case = []
    for case in list(permutations(user_id, len(banned_id))):
        if check(case, banned_id):
            case = set(case)
            if case not in ban_case:
                ban_case.append(case)
    return len(ban_case)


print(solution(["frodo", "fradi", "crodo", "abc123",
      "frodoc"], ["*rodo", "*rodo", "******"]))

# 실패한 풀이


def mul(arr):
    return reduce(lambda x, y: x*y, arr)


def fail_solution(user_id, banned_id):
    banned_count = []

    for b_id in banned_id:
        id_length = len(b_id)
        equal_count = 0
        for u_id in user_id:
            match_count = 0
            if id_length == len(u_id):
                for i in range(len(b_id)):
                    if b_id[i] == u_id[i]:
                        match_count += 1
                    elif b_id[i] == '*':
                        match_count += 1
                if match_count == id_length:
                    equal_count += 1
        banned_count.append(equal_count)

    print(banned_count)
    return mul(banned_count)


print(fail_solution(["frodo", "fradi", "crodo", "abc123",
      "frodoc"], ["*rodo", "*rodo", "******"]))
