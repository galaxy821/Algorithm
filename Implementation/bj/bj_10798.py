"""
세로 읽기 [https://www.acmicpc.net/problem/10798]
"""

if __name__ == "__main__" :
    letter_list = [list(input()) for _ in range(5)] # ABCDE, abcde, 01234, FGHIJ, fghij
    
    result = ""
    for i in range(15) : # 각 문자열 최대 길이는 15
        for j in range(5) : # 5개의 문자열
            if len(letter_list[j]) > i : # 해당 index에 문자열이 존재한다면
                 result += letter_list[j][i] # 해당 문자열의 i번째 문자를 result에 추가

    print(result)