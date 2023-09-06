"""
알파벳 찾기 [https://www.acmicpc.net/problem/10809]
"""

result = [str(-1) for _ in range(21)]

value = input()

for i in range(len(value)) :
    index = ord(value[i])-97
    if result[index] == '-1' :
        result[index]= str(i)
    
print(' '.join(result))