"""
숫자 카드 [https://www.acmicpc.net/problem/10815]
"""
import sys

n = int(input())
card_list = set(map(int, sys.stdin.readline().split()))

m = int(input())
num_list = list(map(int, sys.stdin.readline().split()))

for num in num_list:
    if num in card_list:
        print("1", end=" ")
    else:
        print("0", end=" ")
