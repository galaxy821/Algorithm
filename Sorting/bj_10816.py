"""
숫자 카드 2 [https://www.acmicpc.net/problem/10816]
"""
import sys
n = int(sys.stdin.readline())
data = dict()
for i in list(map(int, sys.stdin.readline().split())):
    if i in data:
        data[i] += 1
    else:
        data[i] = 1
m = int(sys.stdin.readline())
find = list(map(int, sys.stdin.readline().split()))
for i in find:
    if i in data:
        print(data[i], end=" ")
    else:
        print("0", end=" ")

# bineay search
# from bisect import bisect_left, bisect_right

# n = int(input())
# array = list(map(int, input().split()))
# m = int(input())
# targets = list(map(int, input().split()))

# array.sort()

# def find_target_count(array, target) :
#   left = bisect_left(array, target)
#   right = bisect_right(array, target)

#   return right-left

# for i in targets :
#   print(find_target_count(array, i), end=" ")
