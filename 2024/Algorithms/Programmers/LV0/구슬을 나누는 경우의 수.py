from functools import reduce


def solution(balls, share):
    if balls == share:
        return 1
    
    b_fac = reduce(lambda x, y: x * y, range(1, balls + 1))
    s_fac = reduce(lambda x, y: x * y, range(1, share + 1))
    bs_fac = reduce(lambda x, y: x * y, range(1, (balls - share) + 1))
    return b_fac // (bs_fac * s_fac)


"""
factorial 함수 만들기
"""

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


def solution(balls, share):
    return factorial(balls) // (factorial(balls - share) * factorial(share))


import math
def solution(balls, share):
    return math.comb(balls, share)