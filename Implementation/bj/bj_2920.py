"""
음계 [https://www.acmicpc.net/problem/2920]
"""

values = list(map(int, input().split()))

status = ['ascending', 'descending', 'mixed']

if values[0] == 1 :
    status_value = 0
    for i in range(1, len(values)) :
        if values[i-1] > values[i] :
            status_value = 2
            break
elif values[0] == 8 :
    status_value = 1
    for i in range(1, len(values)) :
        if values[i-1] < values[i] :
            status_value = 2
            break
else :
    status_value = 2
    
print(status[status_value])

## 다른 풀이 -> 틀린 풀이 (반례 존재 : 1 2 3 4 6 5 7 8)
"""
def cal_pitch(values) :
    result = 0
    for i in range(1, len(values)) :
        result += ( values[i] - values[i-1])
    print(result)
    return result

if __name__ == "__main__" :
    values =  list(map(int, input().split()))

    result = cal_pitch(values)
    if result == 7 :
        print("ascending")
    elif result == -7 :
        print("descending")
    else :
        print("mixed")
"""