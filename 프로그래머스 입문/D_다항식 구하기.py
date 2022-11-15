def solution(polynomial):
    answer = ''
    x = polynomial
    a = 0
    for i in x.split(' + ') : 
        if 'x' in i : 
            if int(i.replace('x','')) >= 2 : #x가 아닐때 
                a += int(i.replace('x',''))
            else : 
                a += 1 
            answer = f'{a}x'
        else : 
            answer = f'{a}x + {i}'

    return answer

  
  
#다른 사람 코드 (복습 및 공부) 

def solution(polynomial):
    answer = ''
    elements = polynomial.split(' + ')

    count_x, const = 0, 0
    for e in elements:
        if e[-1] == 'x': #상수항이 없을 때 
            if e[:-1]: #x앞에 숫자가 붙어있을 때 
                count_x += int(e[:-1])
            else: #'x'일때 
                count_x += 1
        else:
            const += int(e)

    if count_x and const:
        answer = f'{count_x}x + {const}' if count_x > 1 else f'x + {const}'
    elif count_x and not const:
        answer = f'{count_x}x' if count_x > 1 else 'x'
    else:
        answer = f'{const}'

    return answer
