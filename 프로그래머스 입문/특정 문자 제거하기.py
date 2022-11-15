# 첫 코드
def solution(my_string, letter):
    answer = ''
    for x in range(len(letter)):
        answer = my_string.replace(letter[x],"")
    return answer
  
 
# 두번째 시도 코드
def solution(my_string, letter):
    return my_string.replace(letter, '')
