"""
스택 수열 [https://www.acmicpc.net/problem/1874]
"""

import sys


def cal_stack(n):
    data = [int(sys.stdin.readline()) for _ in range(n)]
    stack = [0 for _ in range(n+1)]
    pointer = 0
    result = []

    for i in data:
        print("current : ", i, result, pointer, stack)
        temp = pointer + 1
        if stack[i] == 0:
            for j in range(temp, i+1):
                if stack[j] == 0:
                    stack[j] = 1
                    result.append('+')
                    pointer += 1
                elif stack[j] == 2:
                    pointer += 1
                else:
                    return False

            stack[i] = 2
            result.append('-')
            pointer -= 1
        elif stack[i] == 1:
            temp = pointer
            for k in range(temp, -1, -1):
                if stack[k] == 2:
                    pointer -= 1
                else:
                    break
            if i == pointer:
                stack[i] = 2
                result.append('-')
                pointer -= 1
                for k in range(i-1, -1, -1):
                    if stack[k] == 2:
                        pointer -= 1
                    else:
                        break
            else:
                return False
        elif stack[i] == 2:
            return False

    return result


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    result = cal_stack(n)
    if result == False:
        sys.stdout.write("NO")
    else:
        for i in result:
            sys.stdout.write("%s\n" % i)
