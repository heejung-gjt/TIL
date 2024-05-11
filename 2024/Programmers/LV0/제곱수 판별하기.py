import math

def solution(n):
    a = math.sqrt(n)
    return 2 if a % int(a) else 1