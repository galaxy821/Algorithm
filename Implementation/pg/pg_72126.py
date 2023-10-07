"""
단속카메라 [https://school.programmers.co.kr/tryouts/72126/challenges?language=python3]
"""


def solution(routes):
    answer = 0
    cur_camera = -30001

    routes.sort(key=lambda x: x[1])

    for route in routes:
        if route[0] > cur_camera:
            answer += 1
            cur_camera = route[1]

    return answer


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
