"""
소수 찾기 [https://www.acmicpc.net/problem/1978]
"""
import math

def is_prime(n) :
    result = True
    if n == 1 :
        return False
    elif n == 2 :
        return True
    for i in range(2, int(math.sqrt(n))+1) :
        if n % i == 0 :
            result = False
            break
    return result

n = int(input())
values = list(map(int, input().split()))
count = 0
for i in values :
    if is_prime(i) :
        count += 1
print(count)