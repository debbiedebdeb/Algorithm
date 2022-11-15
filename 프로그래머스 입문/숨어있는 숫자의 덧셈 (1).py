import re
def solution(my_string):
    answer = sum(map(int, re.findall(r'\d', my_string)))
    return answer
  

#두번째 시도 코드 
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())
