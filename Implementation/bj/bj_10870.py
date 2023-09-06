"""
피보나치 수 5 [https://www.acmicpc.net/problem/10870]
"""

def cal_fibo(n) :
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    
    array = [0] * (n+1)
    array[1] = 1
    
    for i in range(2, n+1) :
        array[i] = array[i-1] + array[i-2]
        
    return array[n]

n = int(input())
print(cal_fibo(n))
