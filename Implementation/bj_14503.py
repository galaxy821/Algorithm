a, b = map(int, input().split())
x, y, d = map(int, input().split())

data_map = []
for _ in range(a) :
  data_map.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visit_map = [[0] * b for _ in range(a)]
visit_map[x][y] = 1

result = 1
turn_time = 0

def turn_left(d) :
    d -= 1
    if d < 0 :
        d = 3
    
    return d

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

print(result)