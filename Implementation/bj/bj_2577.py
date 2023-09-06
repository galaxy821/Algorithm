"""
숫자의 개수 [https://www.acmicpc.net/problem/2577]
"""

a = int(input())
b = int(input())
c = int(input())

sum = a * b * c
result = [0 for _ in range(10)]
for i in str(sum) :
    result[int(i)]+= 1
    
for i in result :
    print(i)
    
## 다른 풀이
"""
value = 1
for i in range(3) :
    temp = int(input())
    value *= temp

sum_str = str(value)
for i in range(10) :
    print(sum_str.count(str(i)))
"""