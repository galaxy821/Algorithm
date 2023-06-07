"""
This is Coding test
이것이 코딩테스트다. 8번

문자열 내 문자가 숫자인지 판별
- isdigit() 함수 사용

리스트 내 원소를 문자열로 합치기
- "".join(list)
"""

if __name__=="__main__":
    n = input()
    
    count_num = 0
    letter_list = []
    
    for i in range(len(n)):
        if n[i].isdigit() == True :
            count_num += int(n[i])
        else :
            letter_list.append(n[i])
            
    letter_list.sort()
    letter_list.append(str(count_num))
    
    print("".join(letter_list))