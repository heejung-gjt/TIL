def solution(id_pw, db):
    db_id = [info[0] for info in db]
    db_pwd = [info[1] for info in db]
    ids, pw = id_pw[0], str(id_pw[1])
    
    for i, p in zip(db_id, db_pwd):
        if ids == i and pw == p:
            return 'login'
        elif ids == i and pw != p:
            return 'wrong pw'
        
    return 'fail'


"""
another
"""

def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"