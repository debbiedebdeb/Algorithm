# 첫 코드  
import math 

def solution(price):
    answer = 0
    x = price
    if price >= 500000 : 
        answer = x*0.8
    elif price >= 300000 :
        answer = x*0.9 
    elif price >= 100000 :
        answer = x*0.95
    elif price >= 10 :
        answer = x 

    answer = math.trunc(answer)
    return answer
  
  
# 2번째 제출한 코드 
def solution(price):
    pd = {500000: 0.8, 300000 : 0.9, 100000 : 0.95, 0 : 1}
    for k,v in pd.items() : 
        if price >= k :
            return int(price*v)
