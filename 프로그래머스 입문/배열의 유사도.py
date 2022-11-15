# 첫번째 코드 
def solution(s1, s2):
    answer = 0
    for s in s1 : 
        if s in s2 : 
            answer +=1
    return answer
  
# 두번쨰 코드 
def solution(s1, s2):
    return len(set(s1)&set(s2));
