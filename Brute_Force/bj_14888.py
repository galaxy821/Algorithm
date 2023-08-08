"""
연산자 끼워넣기
"""

n = int(input())
values = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = int(1e9)
max_value = -int(1e9)


def cal_equation(idx, add, sub, mul, div, result):
    global min_value, max_value
    if idx == n:
        min_value = min(result, min_value)
        max_value = max(result, max_value)
        return

    if add > 0:
        cal_equation(idx+1, add-1, sub, mul, div, result+values[idx])
    if sub > 0:
        cal_equation(idx+1, add, sub-1, mul, div, result-values[idx])
    if mul > 0:
        cal_equation(idx+1, add, sub, mul-1, div, result*values[idx])
    if div > 0:
        cal_equation(idx+1, add, sub, mul, div-1, int(result/values[idx]))


cal_equation(1, add, sub, mul, div, values[0])
print(max_value)
print(min_value)
