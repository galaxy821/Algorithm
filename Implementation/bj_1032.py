"""
명령 프롬프트 [https://www.acmicpc.net/problem/1032]
"""

n = int(input())

for i in range(n) : 
    name = input()
    if i == 0 :
        result = list(name)
    else :
        for j in range(len(name)) :
            if result[j] != name[j] :
                result[j] = '?'

print(''.join(result))