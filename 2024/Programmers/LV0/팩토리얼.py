def solution(n):
    f = 1
    num = 1
    
    while f <= n:
        num += 1
        f *= num
        
    num -= 1

    return num



from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k