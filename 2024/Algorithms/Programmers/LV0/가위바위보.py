def solution(rsp):
    dic = {'2': '0', '0': '5', '5': '2'}
    answer = ''
    for i in list(map(str, rsp)):
        answer += dic[i]
    return answer


def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)


def solution(rsp):
    return rsp.translate(str.maketrans('025', '502'))