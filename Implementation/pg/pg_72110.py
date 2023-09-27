"""
키패드 누르기 [https://school.programmers.co.kr/tryouts/72110/challenges?language=python3]
"""


def solution(numbers, hand):
    pos = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    answer = ''

    r = pos['#']
    l = pos['*']

    for num in numbers:
        cur = pos[num]
        if num in [1, 4, 7]:
            l = cur
            answer += 'L'
        elif num in [3, 6, 9]:
            r = cur
            answer += 'R'
        else:
            l_dist = abs(cur[0]-l[0])+abs(cur[1]-l[1])
            r_dist = abs(cur[0]-r[0])+abs(cur[1]-r[1])

            if l_dist > r_dist:
                r = cur
                answer += 'R'
            elif l_dist < r_dist:
                l = cur
                answer += 'L'
            else:
                if hand == "left":
                    l = cur
                    answer += 'L'
                else:
                    r = cur
                    answer += 'R'

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))  # "LRLLLRLLRRL"
