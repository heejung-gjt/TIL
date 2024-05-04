def solution(a, b, c):
    li = [a, b, c]
    res = len(set(li))
    return a + b + c if res == 3 else (a + b + c) * (a*a + b*b + c*c) if res == 2 else (a + b + c) * (a*a + b*b + c*c) * (a*a*a + b*b*b + c*c*c) 

