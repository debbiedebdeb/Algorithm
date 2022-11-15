def solution(id_pw, db):
    ids = [x[0] for x in db]
    pws = [x[1] for x in db]
    answer = ''
    if id_pw in db : 
        answer = 'login'

    else : 
        if id_pw[0] in ids : 
            answer = 'wrong pw'
        else : 
            answer = 'fail'
    return answer
  

# dict를 이용한 코드
def solution(id_pw, db):
    dic = dict(db)
    if dic.get(id_pw[0],-1) == id_pw[1]:
        return "login"
    elif dic.get(id_pw[0],-1) == -1:
        return "fail"
    else:
        return "wrong pw"
