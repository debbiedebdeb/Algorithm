def solution(sides):
    long = sides.pop( sides.index(max(sides)))
    answer = 1 if long < sum( sides ) else 2
    return answer
  
  
# 두번째 시도 코드 
def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2
