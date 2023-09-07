"""
신규 아이디 추천 [https://school.programmers.co.kr/tryouts/72059/challenges]
"""


def step_2(new_id):

    result = ""
    for word in new_id:
        if word.isalnum() == True or word in "-_.":
            result += word

    return result


def step_3(new_id):
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    return new_id


def step_4(new_id):
    if len(new_id) > 1:
        while new_id[0] == '.' or new_id[-1] == '.':
            if new_id[0] == '.' and new_id[-1] == '.':
                new_id = new_id[1:-1]
            elif new_id[0] == '.':
                new_id = new_id[1:]
            elif new_id[-1] == '.':
                new_id = new_id[:-1]
    else:
        if new_id == '.':
            new_id = ""

    return new_id

    # 짧은 버전
    # new_id = new_id[1:] if new_id[0] == '.' and len(new_id) > 1 else new_id
    # new_id = new_id[:-1] if new_id[-1] == '.' else new_id


def step_5(new_id):
    if len(new_id) == 0:
        return "a"
    else:
        return new_id

    # 짧은 버전
    # new_id = 'a' if new_id == '' else new_id


def step_6(new_id):
    if len(new_id) >= 16:
        return step_4(new_id[:15])
    else:
        return new_id


def step_7(new_id):
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id

    # 짧은 버전
    # new_id = new_id + new_id[-1] * (3-len(new_id))


def solution(new_id):

    new_id = new_id.lower()
    new_id = step_2(new_id)
    new_id = step_3(new_id)
    new_id = step_4(new_id)
    new_id = step_5(new_id)
    new_id = step_6(new_id)
    new_id = step_7(new_id)

    return new_id


print(solution("=.="))
