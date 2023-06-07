"""
로봇 청소기 [https://www.acmicpc.net/problem/14503]
"""

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(d) :
    """turn_left
    
    Args: 
        d (int): 현재 회전 방향
    Returns:
        d (int): 회전 후 방향 
    """
    d -= 1
    if d < 0 :
        d = 3
    
    return d

def cal_cleaned_area(a, b, x, y, d, data_map):
    """cal_cleaned_area
    로봇이 청소하는 잉역의 개수를 구하는 함수

    Args:
        a (int): 방의 세로 크기
        b (int): 방의 가로 크기
        x (int): 로봇의 처음 위치 (행)
        y (int): 로봇의 처음 위치 (열)
        d (int): 로봇의 처음 방향
        data_map (list): 방의 상태 정보
        
    Returns:
        result (int): 청소한 칸의 개수
    """
    visit_map = [[0] * b for _ in range(a)] # 방문한 위치 정보
    visit_map[x][y] = 1 # 현재 위치를 방문 처리
    result = 1 # 청소한 칸의 개수
    turn_time = 0 # 회전한 횟수
    
    while True :
        d = turn_left(d)
        nx = x + dx[d]
        ny = y + dy[d]

        if visit_map[nx][ny] == 0 and data_map[nx][ny] == 0 :
            visit_map[nx][ny] = 1
            x = nx
            y = ny
            result += 1
            turn_time = 0
            continue
        else :
            turn_time += 1

        if turn_time == 4 :
            nx = x - dx[d]
            ny = y - dy[d]

            if data_map[nx][ny] == 0 :
                x = nx
                y = ny
            else :
                break

            turn_time = 0
            
    return result

if __name__ == "__main__" :
    a, b = map(int, input().split()) # 3 <= a, b <= 50
    x, y, d = map(int, input().split()) # 0 <= x <= a-1, 0 <= y <= b-1, 0 <= d <= 3

    data_map = [] # 방의 상태 정보
    for _ in range(a) :
        data_map.append(list(map(int, input().split()))) # 0: 빈 칸, 1: 벽

    result = cal_cleaned_area(a, b, x, y, d, data_map)
    print(result)