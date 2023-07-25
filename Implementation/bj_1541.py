"""
잃어버린 괄호 [https://www.acmicpc.net/problem/1541]
"""

exp = input()

result = 0
temp_exp = 0
temp = ""
isMinusMode = False

for i in exp:
    if i == "-" and not isMinusMode:
        isMinusMode = True
        temp_exp += int(temp)
        result += temp_exp
        temp_exp = 0
        temp = ""
    elif i == "-" and isMinusMode:
        temp_exp += int(temp)
        result -= temp_exp
        temp_exp = 0
        temp = ""
    elif i == '+':
        temp_exp += int(temp)
        temp = ""
    else:
        temp += i

if isMinusMode:
    result -= temp_exp
    result -= int(temp)
else:
    result += temp_exp
    result += int(temp)
print(result)
