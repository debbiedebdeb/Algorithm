def solution(n):
    for i in range(1,100) : 
        if (i*6)%n ==0 : 
            answer = i
            break 
    return answer
  
  
# 다른 코드
def solution(n):
    i=1
    while(1):
        if (6*i)%n==0:
            return i
        i+=1
