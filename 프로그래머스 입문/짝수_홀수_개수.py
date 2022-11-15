# 내 코드 
def solution(num_list):
    answer = []
    even_ = 0
    odds_ = 0
    for i in num_list : 
        if i%2 == 0 : 
            even_ += 1
        else : 
            odds_ += 1
    answer.append(even_)
    answer.append(odds_)
   
# 2번째 시도 코드 
def solution(num_list):
    div_num_list = list(map(lambda v: v % 2, num_list))
    return [div_num_list.count(0), div_num_list.count(1)]
    
    
    
# 3번째 시도 코드 
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer
