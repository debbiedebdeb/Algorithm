def solution(my_string, n):
    answer = ''
    for i in list(my_string): 
        answer += i*n
    
    return answer

#두번째 코드 
def solution(my_string, n):
    return ''.join(i*n for i in my_string)
