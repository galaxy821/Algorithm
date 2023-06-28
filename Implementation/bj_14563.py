"""
완전수 [https://www.acmicpc.net/problem/14563]
"""
import math

def cal_sum_divisor(n) :
    sum = 1
    for i in range(2, int(math.sqrt(n))+1) :
        if n % i == 0 :
            sum += i
            value = n // i
            if i != value :
                sum += value
    return sum

n = int(input())
values = list(map(int, input().split()))

for value in values :
    result = cal_sum_divisor(value)
    if result == value :
        print("Perfect")
    elif result < value :
        print("Deficient")
    else :
        print( "Abundant")