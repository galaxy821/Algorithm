"""
[카카오 인턴]보석 쇼핑 [https://school.programmers.co.kr/tryouts/72097/challenges]
"""


def solution(gems):
    N = len(gems)
    answer = [0, N-1]
    kind = len(set(gems))
    dic = {gems[0]: 1}
    s, e = 0, 0

    while s < N and e < N:
        if len(dic) < kind:
            e += 1
            if e == N:
                break
            dic[gems[e]] = dic.get(gems[e], 0)+1

        else:
            if (e-s) < (answer[1] - answer[0]):
                answer = [s, e]
            if dic[gems[s]] == 1:
                del dic[gems[s]]
            else:
                dic[gems[s]] -= 1
            s += 1

    return [answer[0]+1, answer[1]+1]


# 효율성 나락 코드ㅠ
def solution2(gems):
    n_gems = len(set(gems))

    min_len = len(gems)
    min_start = len(gems)
    min_end = 0

    start = 0
    end = 0

    while end < len(gems):
        if len(set(gems[start:end+1])) < n_gems:
            end += 1
        else:
            if (end-start + 1) < min_len:
                min_len = (end-start + 1)
                min_start = start
                min_end = end
            elif (end-start + 1) == min_len and start < min_start:
                min_start = start
                min_end = end

            if start < end:
                start += 1
            else:
                end += 1

    return [min_start+1, min_end+1]


print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
