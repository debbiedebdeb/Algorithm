def solution(numlist, n):
    for i in numlist : 
        answers.append((i, abs(i - n)) ) 
    answers = sorted(answers,key = lambda x : (x[1],-x[0]) ) 
    answer = []
    for x in answers : 
        answer.append(x[0])
    return answer
  

  
# 공부 및 복습했던 코드 
def solution(numlist, n):
    numlist.sort(key=lambda x: (abs(n - x), -x))
    return numlist
