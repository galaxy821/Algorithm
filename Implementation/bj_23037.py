"""
5의 수난 [https://www.acmicpc.net/problem/23037]
"""

n = input()

result = 0
for i in n :
    result += int(i)**5
    
print(result)