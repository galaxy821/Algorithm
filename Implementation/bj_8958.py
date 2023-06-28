"""
OX 퀴즈 [https://www.acmicpc.net/problem/8958]
"""

n = int(input())

for _ in range(n) :
    test_case = input()
    sum_value = 0
    acc_value = 0
    for i in range(len(test_case)) :
        if test_case[i] == 'O' :
            acc_value += 1
            sum_value += acc_value
        else :
            acc_value =0
    print(sum_value)