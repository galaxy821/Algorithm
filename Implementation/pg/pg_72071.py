"""
수식 최대화 [https://school.programmers.co.kr/tryouts/72071/challenges?language=python3]
"""

from collections import deque
from itertools import permutations


def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))


def calculate(exp, op):
    array = deque()
    tmp = ""

    for i in exp:
        if i.isdigit() == True:
            tmp += i
        else:
            array.append(tmp)
            array.append(i)
            tmp = ""

    array.append(tmp)

    for o in op:
        stack = deque()
        while len(array) != 0:
            print(stack, o)
            tmp = array.popleft()
            if tmp == o:
                stack.append(operation(stack.pop(), array.popleft(), o))
            else:
                stack.append(tmp)
        array = stack

    return abs(int(array[0]))


def solution(expression):
    op = ['+', '-', '*']
    op = list(permutations(op, 3))
    result = []
    for i in op:
        result.append(calculate(expression, i))
    return max(result)


print(solution("100-200*300-500+20"))
