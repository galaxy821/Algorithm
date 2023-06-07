"""
럭키 스트레이트 [https://www.acmicpc.net/problem/18406]
"""

if __name__ == "__main__" :
    n = input() # 123402, 7755

    front_count = 0
    back_count = 0

    for i in range(int(len(n)/2)) :
        front_count += int(n[i])
        back_count += int(n[-i-1])

    if front_count == back_count :
        print("LUCKY") # anwser of 123402
    else :
        print("READY") # anwser of 7755