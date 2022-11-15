def solution(n) : 
    answer = 0
    for i in range(1,n+1) : 
        if n%i ==0 :
            answer += 1 
    return answer
  
#2번째 코드
def solition(n) : 
    answer = len[i for i in range(1,n+1) if n%i ==0]

    return answer
