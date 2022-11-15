def solution(n):
    answer = 0 
    for i in list(str(n)) :
        answer += int(i)
    
    return answer
  
# 2번째 코드 
def solution(n):
    answer = sum( map(int, list(str(n)))  )
    return answer
