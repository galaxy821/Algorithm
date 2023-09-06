"""
[삼각달팽이] https://school.programmers.co.kr/tryouts/72049/challenges
"""

# 정삼각형 형태의 데이터를 왼쪽으로 치우친 직각삼각형 형태의 2차원 리스트로 만든 다음 결과를 도출한다.
# 삼각형을 둘러싸는 한변 한변 마다 분리한다. (방향별로)
# 예를 들어 n = 4일 때 [1,2,3,4], [5,6,7], [8,9], [10]으로 방향별 삼각형의 한변을 분리할 수 있다.
# 삼각형 한바퀴 도는데 세개의 변을 거처야 하므로 (위에서 나눈 삼각형 변의 개수 => N이라고 하자) % 3 으로 현재 해당 변의 방향을 구할 수 있다.
# N % 3 == 0일 때는 아래로 항하는 변이며, N % 3 == 1일 때는 우측으로 향하는 변이며, N % 3 == 2일 때는 좌상단을 향하는 변이다.

# 참고한 글 : https://moondol-ai.tistory.com/395


def solution(n):
    data = [[0]*n for _ in range(n)]

    x, y = -1, 0
    index = 1

    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            data[x][y] = index
            index += 1

    answer = []
    for i in range(n):
        for j in range(n):
            answer.append(data[i][j])

    return answer


solution(6)

# input : 4
# output : [1,2,9,3,10,8,4,5,6,7]

# input : 5
# output : [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]

# input : 6
# output : [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
