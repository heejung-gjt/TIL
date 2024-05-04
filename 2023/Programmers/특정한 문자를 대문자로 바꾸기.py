def solution(my_string, alp):
    res = ''
    for i in my_string:
        if i == alp:
           res += i.upper()
        else:
            res += i
    return res

# sol1
#def solution(my_string, alp):
#    return my_string.replace(alp, alp.upper())