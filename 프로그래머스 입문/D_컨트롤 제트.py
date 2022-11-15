def solution(s):
    answer = []

    for i in s.split() :
        if i != 'Z' :
            answer.append(i)
        else :
            answer.pop()

    return sum(map(int, answer))
solution(s)
