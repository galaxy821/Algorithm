"""
더하기 사이클 [acmicpc.net/problem/1110]
"""

n = int(input())
cur_value = n
result = 1

while True:
    if cur_value < 10:
        front_val = 0
        back_val = cur_value
    else:
        front_val = cur_value // 10
        back_val = cur_value % 10
    new_value = front_val + back_val
    cur_value = back_val*10 + new_value % 10
    if cur_value == n:
        break
    result += 1

print(result)
