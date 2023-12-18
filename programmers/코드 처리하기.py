"""
code[i]가 1이면 mode -> 0으로 변경한다
mode = 0일때 -> code[i]가 1이 아니고 짝수이면 code[idx]뒤에 해당 문자열 추가한다
mode = 1일때 -> code[i]가 1이 아니고 홀수이면 code[idx]뒤에 해당 문자열 추가한다
"""
def solution(code):
    mode = 0
    ret = ''
    for i, j in enumerate(code):
        if not mode:
            if j == "1":
                mode = 1
            if j != "1" and i % 2 == 0:
                ret += j
        else:
            if j == "1":
                mode = 0
            if j != "1" and i % 2 == 1:
                ret += j
    
    return ret if ret else "EMPTY"

# sol1 
#def solution(code):
#    return "".join(code.split("1"))[::2] or "EMPTY"


# sol2
# def solution(code):
#     answer = ''

#     mode = 0
#     for i in range(len(code)):
#         if code[i] == '1':
#             mode ^= 1
#         else:
#             if i % 2 == mode:
#                 answer += code[i]

#     return answer if answer else 'EMPTY'