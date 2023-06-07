# baekjooon 2839
n = int(input())
sugar = [5,3]
result = 10e9

for count in range(n//sugar[0]+1):
    left = n - count*sugar[0]
    if left % sugar[1] == 0 :
        result = min(result, count + left//sugar[1])
    
if(result == 10e9):
    print(-1)
else :
    print(result)