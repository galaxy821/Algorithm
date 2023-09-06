"""
제로 [https://www.acmicpc.net/problem/10773]
"""

if __name__=="__main__" :
    n = int(input()) # 4
    money_list = []
    for _ in range(n) :
        money = int(input()) # 3, 0, 4, 0
        if money == 0 :
            money_list.pop()
        else :
            money_list.append(money)
            
    print(sum(money_list)) # 0
    