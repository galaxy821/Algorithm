"""
프린터 큐 [https://www.acmicpc.net/problem/1966]
"""
from collections import deque

if __name__ == "__main__" :
    n = int(input()) # 테스크 케이스 개수
    
    for _ in range(n):
        num_doc, num_target = map(int, input().split()) # 문서의 개수, 몇 번째로 인쇄되었는지 궁금한 문서의 현재 위치
        priority_list = deque(zip(range(num_doc),map(int, input().split()))) # 문서 리스트
        
        count = 0
        
        while True :
            if len(priority_list) == 1:
                count += 1
                break
            
            current_doc, current_priority = priority_list.popleft()
            if current_priority >= max(priority_list, key = lambda x : x[1])[1] :
                count += 1
                if current_doc == num_target :
                    break
                else :
                    continue
            else :
                priority_list.append((current_doc, current_priority))
                
        print(count)