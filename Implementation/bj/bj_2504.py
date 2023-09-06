"""
괄호의 값
"""

a = input()


def check_bracket(s):
    stack = []

    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        elif s[i] == ')':
            if len(stack) > 0:
                temp = stack.pop()
                if temp != "(":
                    return False
            else:
                return False
        elif s[i] == ']':
            if len(stack) > 0:
                temp = stack.pop()
                if temp != "[":
                    return False
            else:
                return False
    if len(stack) > 0:
        return False
    else:
        return True


def cal_bracket(s):
    stack = []
    result = 0

    for i in range(len(s)):
        sum = 0

        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        elif s[i] == ')':
            while True:
                temp = stack.pop()
                if temp == '(':
                    break
                sum += temp
            if sum == 0:
                sum = 1
            stack.append(2*sum)
        elif s[i] == ']':
            while True:
                temp = stack.pop()
                if temp == '[':
                    break
                sum += temp
            if sum == 0:
                sum = 1
            stack.append(3*sum)
    while stack:
        result += stack.pop()

    return result


if check_bracket(a):
    print(cal_bracket(a), end='\n')
else:
    print(0, end='\n')
