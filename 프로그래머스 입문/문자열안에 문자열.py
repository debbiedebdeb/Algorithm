# 첫시도 코드 
def solution(str1, str2):
    answer = 0
    if str2 in str1 :
        answer = 1
    else : 
        answer = 2
    return answer
  
# 두번째 코드
def solution(str1, str2):
    return 1 if str2 in str1 else 2
