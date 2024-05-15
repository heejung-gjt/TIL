def solution(s):
    ss = s.split(' ')
    while 'Z' in ss:
        idx = ss.index('Z')
        ss.pop(idx)
        ss.pop(idx - 1)
        
    return sum(map(lambda x: int(x), ss))




"""
stack 특징 활용
"""
def solution(s):
    stack = []
    for i in s.split():
        if i != 'Z':
            stack.append(int(i))
        else:
            if stack:
                stack.pop()

    return sum(stack)